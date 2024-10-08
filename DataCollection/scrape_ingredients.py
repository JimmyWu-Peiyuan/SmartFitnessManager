from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.options import Options


# Reference: In this part, anything related to the usage of selenium package is under help with ChatGPT.

def parse_ingredients_page(url_driver):
    # Initialize a list to store the data
    data_list = []

    while True:
        # Get the entire HTML source code from the page by using driver to mimic users' behaviour
        html = url_driver.page_source
        # Parse html with BeautifulSoup
        soup = BeautifulSoup(html, 'lxml')

        # Find the table in the page, reference: slides week 2
        table_list = soup.findAll('table')
        table = table_list[0]  # only one table

        # Extract table content, including hyperlinks
        rows = table.findAll('tr')
        for row in rows:
            cols = row.findAll('td')
            data = []
            for col in cols:
                # only one column has a hyperlink
                # Reference: ChatGPT
                link = col.find('a')
                if link:
                    # extract link and text separately
                    href = link['href']
                    text = link.text.strip()
                    data.append(text)
                    data.append(href)
                else:
                    data.append(col.text.strip())
            data_list.append(data)

        # Try to find the next page link and click it
        # Reference: ChatGPT
        try:
            # Find all page links
            page_links = url_driver.find_elements(By.XPATH, '//div[@_ngcontent-c3=""]/a')
            # Check for the current page
            current_page = None
            for link in page_links:
                if 'current' in link.get_attribute('class'):
                    current_page = link
                    break

            # Click on the next page link (if it exists)
            if current_page is not None:
                next_index = page_links.index(current_page) + 1  # Get the index of the next page link
                if next_index < len(page_links):  # Check if there's a next page
                    page_links[next_index].click()  # Click on the next page
                    time.sleep(3)  # Wait for the page to load
                else:
                    break  # No more pages to click
        except Exception as e:
            print("No more pages or an error occurred:", e)
            break  # Break the loop if there's an error

    return data_list

def scrape_ingredients():
    # Set up Chrome options to run in headless mode
    chrome_options = Options()
    # "--headless": # to block the Chrome window not to pop up during scraping, reference: chatgpt
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # Start Chrome driver in headless mode
    driver = webdriver.Chrome(options=chrome_options)
    url = 'https://fdc.nal.usda.gov/fdc-app.html#/food-search?type=Foundation&query='
    driver.get(url)
    time.sleep(3)


    data_list = parse_ingredients_page(driver)

    driver.quit()

    # store cleaned data to csv
    data_list[0] = ["NDB Number", "Description", "Links of Details", "Most Recent Acquisition Date", "SR/Foundation Food Category"]  # Add headers
    df = pd.DataFrame(data_list[1:], columns=data_list[0])
    df["Links of Details #"] = df["Links of Details"].str.extract(r'/food-details/(\d+)/nutrients')
    df.dropna(inplace=True)
    return df
