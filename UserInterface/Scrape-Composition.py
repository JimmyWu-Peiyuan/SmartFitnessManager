import pandas as pd
from selenium import webdriver
import time
from bs4 import BeautifulSoup

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
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    data_list = parse_composition_page(driver)
    driver.quit()

    filtered_data = [row for row in data_list if row and row[0] in
                     ["Water", "Energy (Atwater General Factors)", "Protein"]]

    return filtered_data

# Reference: ChatGPT
def user_interface():
    # "dtype={"NDB Number": str}" is added because I found when python read a cav file,
    # it will treat any number as float by default, but we need it to be string when being a part of url link
    ingredients_table = pd.read_csv("ingredients.csv", dtype={"Links of Details #": str})
    # let users input their ingredients intake
    ingredients = []
    while True:
        user_input = input("Please enter an ingredient（enter 'end' to end input): \n")
        if user_input.lower() == 'end':
            break
        ingredients.append(user_input)

    for ingredient in ingredients:
        match = ingredients_table[ingredients_table["Description"].str.contains(ingredient, case=False, na=False)]
        if not match.empty:
            ndb_number = match.iloc[0]["Links of Details #"]
            url = f'https://fdc.nal.usda.gov/fdc-app.html#/food-details/{ndb_number}/nutrients'
            filtered_data = get_composition_data(url)
            print("Nutritional Composition of", ingredient, "is:")
            for item in filtered_data:
                print(item[0],item[1],item[2])
            print("\n")
        else:
            print(f"No matching ingredient found for '{ingredient}' in the ingredients table.")

if __name__ == '__main__':
    user_interface()