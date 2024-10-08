import pandas as pd
from matplotlib import pyplot as plt
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

# Reference: In this part, anything related to the usage of selenium package is under help with ChatGPT.

def parse_composition_page(url_driver):
    # Initialize a list to store the data
    data_list = []

    # Get the HTML source code from the page
    html = url_driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    # Find the table in the page
    tables = soup.find_all('table')

    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            data = []
            for col in cols:
                data.append(col.text.strip())
            data_list.append(data)

    return data_list

def get_composition_data(url):
    # Set up Chrome options to run in headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless') # to block the Chrome window not to pop up during scraping, reference: chatgpt
    chrome_options.add_argument('--disable-gpu')

    # Start Chrome driver in headless mode
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)
    time.sleep(3)
    data_list = parse_composition_page(driver)
    driver.quit()

    filtered_data = [row for row in data_list if row and row[0] in
                     ["Water", "Energy (Atwater General Factors)", "Protein"]]

    return filtered_data

def geturl(user_input, ingredients_table): 
    match = ingredients_table[ingredients_table["Description"].str.contains
                        (user_input, case=False, na=False, regex=False)]
    if not match.empty:
        ndb_number = match.iloc[0]["Links of Details #"]
        url = f'https://fdc.nal.usda.gov/fdc-app.html#/food-details/{ndb_number}/nutrients'
        return url
    else:
        return None



def user_interface():
    ingredients_table = pd.read_csv("ScrapedData/ingredients.csv", dtype={"Links of Details #": str})

    daily_totals_list = []
    i = 1 # initialize day

    # Reference: This double while loop is edited based on the results from chatgpt
    while True:
        day_totals = {'Water': 0, 'Energy': 0, 'Protein': 0}
        ingredients = []

        user_input = input(
            f"Please enter an ingredient for day {i} (enter 'end' to end today's input, 'analyse' to analyse, or 'exit' to exit): \n")

        if user_input.lower() == 'exit':
            break

        while user_input.lower() != 'end':
            if user_input.lower() == 'analyse':
                generate_charts(daily_totals_list)
                user_input = input(f"Please enter an ingredient for day{i} (enter 'end' to end today's input, 'analyse' to analyse): \n")
                continue

            ingredients.append(user_input)

            try:
                amount = float(input(f"Enter the amount of **{user_input}** consumed for day **{i}**: \n"))
                match = ingredients_table[ingredients_table["Description"].str.contains
                        (user_input, case=False, na=False, regex=False)]
                # "regex=False" is to avoid Python treating special characters as regularization pattern, reference: ChatGPT
                if not match.empty:
                    # Real-time crape and parse nutritional composition of ingredients from user's input
                    
                    filtered_data = get_composition_data(geturl(user_input, ingredients_table))

                    # Record the accumulated nutritional data of users
                    daily_water, daily_energy, daily_protein = 0, 0, 0
                    for item in filtered_data:
                        if item[0] == 'Water':
                            daily_water = float(item[1]) * amount
                        elif item[0] == 'Energy (Atwater General Factors)':
                            daily_energy = float(item[1]) * amount
                        elif item[0] == 'Protein':
                            daily_protein = float(item[1]) * amount
                        print(f"{item[0]}: {item[1]} {item[2]}")

                    day_totals['Water'] += daily_water
                    day_totals['Energy'] += daily_energy
                    day_totals['Protein'] += daily_protein
                else:
                    print(f"No matching ingredient found for '{user_input}' in the ingredients table.")
            except ValueError:
                print("Invalid input for amount. Please enter a valid number.")

            user_input = input("Please enter another ingredient or 'end' to finish today's input: \n")

        # Store the daily totals for analysis later
        if user_input.lower() == 'end':
            daily_totals_list.append(day_totals)
            print(
                f"Today's totals: Water: {day_totals['Water']}, Energy: {day_totals['Energy']}, Protein: {day_totals['Protein']}")
            print("\n")
        i += 1



# Reference: This plotting function is edited based on the results from chatgpt
def generate_charts(daily_totals_list):
    days = list(range(1, len(daily_totals_list) + 1))
    water_totals = [day['Water'] for day in daily_totals_list]
    energy_totals = [day['Energy'] for day in daily_totals_list]
    protein_totals = [day['Protein'] for day in daily_totals_list]

    # Line chart for daily trends
    plt.figure(figsize=(10, 5))
    plt.plot(days, water_totals, label='Water (g)', marker='o')
    plt.plot(days, energy_totals, label='Energy (kcal)', marker='o')
    plt.plot(days, protein_totals, label='Protein (g)', marker='o')
    plt.xlabel('Days')
    plt.xticks(days)
    plt.ylabel('Amount')
    plt.title('Daily Macronutrient Trends')
    plt.legend()
    plt.show()

    # Pie chart for total nutrient distribution
    total_water = sum(water_totals)
    total_energy = sum(energy_totals)
    total_protein = sum(protein_totals)

    total_data = [total_water, total_energy, total_protein]
    labels = ['Water (g)', 'Energy (kcal)', 'Protein (g)']

    plt.figure(figsize=(7, 7))
    plt.pie(total_data, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Total Macronutrient Distribution')
    plt.show()

if __name__ == "__main__":
    user_interface()