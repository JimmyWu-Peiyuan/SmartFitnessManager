# Code block to scrape, clean and store muscle building programs

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_muscle_programs():
    # Set up the Selenium WebDriver
    driver = webdriver.Chrome()  # Make sure ChromeDriver is installed and in your PATH

    # List of URLs to scrape for muscle building programs
    urls = [
        'https://www.muscleandstrength.com/workouts/muscle-building',
        'https://www.muscleandstrength.com/workouts/muscle-building?page=1',
        'https://www.muscleandstrength.com/workouts/muscle-building?page=2',
        'https://www.muscleandstrength.com/workouts/muscle-building?page=3',
        'https://www.muscleandstrength.com/workouts/muscle-building?page=4',
    ]

    # Use a set to remove repetitions
    workout_links = set()

    # Loop through each URL
    for url in urls:
        # Open the page
        driver.get(url)
        
        # Wait for the dynamic content to load (adjust the sleep time if needed)
        time.sleep(5)
        
        # Get the page source
        page_source = driver.page_source
        
        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')
        
        # Find all <a> tags
        all_links = soup.find_all('a')
        
        # Filter the workout subheadings (hyperlinks)
        for link in all_links:
            href = link.get('href')
            if href and '/workouts/' in href and '/muscle-building' not in href:  # Filter out '/muscle-building' and repetitions
                workout_links.add(href)

    # Extract only the part after 'workouts/' and eliminate those ending with '.html', 'men', 'women', and 'home'
    workout_subpaths = [link.split('/workouts/')[-1] for link in workout_links 
                        if not link.endswith('.html') 
                        and link.split('/workouts/')[-1] not in ['men', 'women', 'home']
                        and not link.split('/workouts/')[-1].startswith('muscle-building?')]

    # Initialize a list to store workout details
    workout_data = []

    # Base URL for all the workouts
    base_url = 'https://www.muscleandstrength.com/workouts/'

    # Loop through each workout and scrape its details
    for i, workout in enumerate(workout_subpaths, start=1):
        # Construct the full URL
        url = base_url + workout

        # Open the page
        driver.get(url)
        
        # Wait for the dynamic content to load
        time.sleep(5)
        
        # Get the page source
        page_source = driver.page_source
        
        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')
        
        # Find the workout summary block
        summary_block = soup.find('div', class_='node-stats-block')
        
        # Extract workout details safely with conditionals
        if summary_block:
            workout_type = summary_block.find('div', class_='field-name-field-workout-type').text.strip() if summary_block.find('div', class_='field-name-field-workout-type') else 'N/A'
            training_level = summary_block.find('div', class_='field-name-field-experience-level').text.strip() if summary_block.find('div', class_='field-name-field-experience-level') else 'N/A'
            
            # Program Duration
            program_duration_element = summary_block.find_all('li')
            program_duration = 'N/A'
            for li in program_duration_element:
                if 'Program Duration' in li.text:
                    program_duration = li.text.split('Program Duration')[-1].strip()
            
            # Days Per Week
            days_per_week = summary_block.find('div', class_='field-name-field-days-per-week').text.strip() if summary_block.find('div', class_='field-name-field-days-per-week') else 'N/A'
            
            # Time Per Workout
            time_per_workout = 'N/A'
            for li in program_duration_element:
                if 'Time Per Workout' in li.text:
                    time_per_workout = li.text.split('Time Per Workout')[-1].strip()
            
            # Equipment Required
            equipment_element = summary_block.find_all('li')
            equipment_required = 'N/A'
            for li in equipment_element:
                if 'Equipment Required' in li.text:
                    equipment_required = li.text.split('Equipment Required')[-1].strip()
            
            # Target Gender
            target_gender = 'N/A'
            for li in equipment_element:
                if 'Target Gender' in li.text:
                    target_gender = li.text.split('Target Gender')[-1].strip()
            
            # Append the data to workout_data list
            workout_data.append({
                'Sr No': i,
                'Program Name': workout.replace('-', ' ').title(),
                'URL': url,
                'Workout Type': workout_type,
                'Training Level': training_level,
                'Program Duration': program_duration,
                'Days Per Week': days_per_week,
                'Time Per Workout': time_per_workout,
                'Equipment Required': equipment_required,
                'Target Gender': target_gender
            })

    # Close the WebDriver
    driver.quit()

    # Create a DataFrame from the workout data
    df = pd.DataFrame(workout_data)
    return df 
# Save the DataFrame to an Excel file with added columns Sr No and Program Name
# df.to_excel('Muscle_and_Strength_Workout_Programs_2.xlsx', index=False)

# print("Excel file created successfully!")
