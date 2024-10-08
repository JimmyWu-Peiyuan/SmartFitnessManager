import tkinter as tk
from tkinter import ttk, messagebox,simpledialog
from DataCollection import weather_api 
import Diet_interface_analysis as diet
import dataprocessing
import pandas as pd
import random
# pip install lxml

class FitnessApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Fitness Tracker")
        self.master.geometry("500x400")
        self.main_frame = ttk.Frame(self.master, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.data = None
        self.intakeurl = None
        self.create_selection_view()

    def create_selection_view(self):
        ttk.Label(self.main_frame, text="Welcome to My SmartFitness Manager!", font=("Arial", 16)).grid(column=0, row=0, columnspan=2, pady=10)
        ttk.Label(self.main_frame, text="Do you prefer to use downloaded data or scrape new data?", font=("Arial", 16)).grid(column=0, row=1, columnspan=2, pady=10)
        ttk.Button(self.main_frame, text="Use existing data", command=self.load_data_view).grid(column=0, row=2, pady=5, padx=5, sticky=tk.W+tk.E)
        ttk.Button(self.main_frame, text="Scrape new data", command=self.scrape_data_view).grid(column=1, row=2, pady=5, padx=5, sticky=tk.W+tk.E)

    def create_main_view(self):
        self.clear_frame()
        ttk.Label(self.main_frame, text="Welcome to My SmartFitness Manager!", font=("Arial", 16)).grid(column=0, row=0, columnspan=2, pady=10)
        ttk.Button(self.main_frame, text="Track Calories", command=self.create_calories_view).grid(column=0, row=1, pady=5, padx=5, sticky=tk.W+tk.E)
        ttk.Button(self.main_frame, text="Workout Recommendations", command=self.create_workout_view).grid(column=0, row=2, pady=5, padx=5, sticky=tk.W+tk.E)
        ttk.Button(self.main_frame, text="Exit", command=self.master.quit).grid(column=0, row=3, pady=5, padx=5, sticky=tk.W+tk.E)

    def create_calories_view(self):
        self.clear_frame()
        self.intakeurl = []
        ttk.Label(self.main_frame, text="Calories Tracker", font=("Arial", 16)).grid(column=0, row=0, columnspan=2, pady=10)
        ttk.Label(self.main_frame, text="Enter food name in 1ct", font=("Arial", 12)).grid(column=0, row=1, columnspan=2, pady=10)
        self.name_entry = ttk.Entry(self.main_frame, width=30)
        self.name_entry.grid(column=0, row=2, sticky=tk.W, pady=5)
        
        ttk.Button(self.main_frame, text="Add food", command=self.add_food).grid(column=0, row=3, columnspan=2, pady=5, padx=5, sticky=tk.W+tk.E)
        if self.intakeurl != None or self.intakeurl != []:
            ttk.Button(self.main_frame, text="Calculate Nutrition facts", command=self.calculate_nutrition_view).grid(column=0, row=4, columnspan=2, pady=5, padx=5, sticky=tk.W+tk.E)
        ttk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_view).grid(column=0, row=5, columnspan=2, pady=5, padx=5, sticky=tk.W+tk.E)

    def add_food(self):
        food_name = self.name_entry.get().lower()
        url = diet.geturl(food_name, self.data.ingredients)
        if url is None:
            messagebox.showinfo("Error", "Food not found.")
        else:
            self.intakeurl.append(url)
            messagebox.showinfo("Success", f"Added {food_name} to the list.")
            self.name_entry.delete(0, tk.END)  # Clear the entry field after adding
   
    def calculate_nutrition_view(self):
        self.clear_frame()
        ttk.Label(self.main_frame, text="Calculating....", font=("Arial", 16)).grid(column=0, row=0, columnspan=2, pady=10)
        day_totals = {'Water': 0, 'Energy': 0, 'Protein': 0}
        for link in self.intakeurl:
            data = diet.get_composition_data(link)
            daily_water, daily_energy, daily_protein = 0, 0, 0
            for item in data:
                if item[0] == 'Water':
                    daily_water = float(item[1])
                elif item[0] == 'Energy (Atwater General Factors)':
                    daily_energy = float(item[1])
                elif item[0] == 'Protein':
                    daily_protein = float(item[1])
            day_totals['Water'] += daily_water
            day_totals['Energy'] += daily_energy
            day_totals['Protein'] += daily_protein
        self.clear_frame()
        ttk.Label(self.main_frame, text=f"Today's totals: Water: {day_totals['Water']}, Energy: {day_totals['Energy']}, Protein: {day_totals['Protein']}", font=("Arial", 13)).grid(column=0, row=0, columnspan=2, pady=10)
        ttk.Button(self.main_frame, text="Track Calories", command=self.create_calories_view).grid(column=0, row=1, pady=5, padx=5, sticky=tk.W+tk.E)
        ttk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_view).grid(column=0, row=2, pady=5, padx=5, sticky=tk.W+tk.E)


    def create_workout_view(self):
        self.clear_frame()
        ttk.Label(self.main_frame, text="Select the Type of Workout", font=("Arial", 16)).grid(column=0, row=0, columnspan=2, pady=10)
        ttk.Button(self.main_frame, text="Get Workout Program", command=self.create_program_view).grid(column=0, row=1, pady=5, padx=5, sticky=tk.W+tk.E)
        ttk.Button(self.main_frame, text="Get Workout Movements", command=self.get_workout_movements).grid(column=0, row=2, pady=5, padx=5, sticky=tk.W+tk.E)
        ttk.Button(self.main_frame, text="Outdoor Activities", command=self.outdoor_activities).grid(column=0, row=3, pady=5, padx=5, sticky=tk.W+tk.E)
        ttk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_view).grid(column=0, row=4, pady=5, padx=5, sticky=tk.W+tk.E)

    def create_program_view(self):
        self.clear_frame()
        ttk.Label(self.main_frame, text="Select Workout Program", font=("Arial", 16)).grid(column=0, row=0, columnspan=2, pady=10)

        ttk.Label(self.main_frame, text="Goal:").grid(column=0, row=1, sticky=tk.W, pady=5)
        self.goal_dropdown = ttk.Combobox(self.main_frame, values=["fatloss", "musclebuilding", "athome"])
        self.goal_dropdown.grid(column=1, row=1, sticky=tk.W, pady=5)
        self.goal_dropdown.set("fatloss")  # Set a default value

        ttk.Label(self.main_frame, text="Difficulty:").grid(column=0, row=2, sticky=tk.W, pady=5)
        self.difficulty_dropdown = ttk.Combobox(self.main_frame, values=["Beginner", "Intermediate", "Advanced"])
        self.difficulty_dropdown.grid(column=1, row=2, sticky=tk.W, pady=5)
        self.difficulty_dropdown.set("Beginner")  # Set a default value

        ttk.Label(self.main_frame, text="Gender:").grid(column=0, row=3, sticky=tk.W, pady=5)
        self.gender_dropdown = ttk.Combobox(self.main_frame, values=["Male", "Female"])
        self.gender_dropdown.grid(column=1, row=3, sticky=tk.W, pady=5)
        self.gender_dropdown.set("Male")  # Set a default value

        ttk.Button(self.main_frame, text="Find Program", command=self.find_program).grid(column=0, row=4, columnspan=2, pady=10)
        ttk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_view).grid(column=0, row=5, columnspan=2, pady=5)

    def find_program(self):
        goal = self.goal_dropdown.get().strip().lower()
        difficulty = self.difficulty_dropdown.get().strip()
        gender = self.gender_dropdown.get().strip()
        self.display_random_program(goal, difficulty, gender)

    def display_random_program(self, goal, difficulty, gender):
        self.clear_frame()
        try:
            programs = self.data.getPrograms(goal, difficulty, gender)
            if not programs:
                messagebox.showinfo("No Programs", "No programs found for the selected criteria.")
                self.create_program_view()
                return
            
            program = random.choice(programs)

            ttk.Label(self.main_frame, text="Recommended Workout Program", font=("Arial", 16)).grid(column=0, row=0, columnspan=2, pady=10)

            # Create a Text widget to display program details
            
            text_widget = tk.Text(self.main_frame, wrap=tk.WORD, width=60, height=12)
            text_widget.grid(column=0, row=1, columnspan=2, pady=5, padx=5, sticky="nsew")

            # Insert program details into the Text widget
            details = f"Program Name: {program.get('Program Name', 'Unnamed Program')}\n"
            details += f"URL: {program.get('URL', 'N/A')}\n\n"
            details += f"Difficulty: {program.get('Training Level', 'N/A')}\n"
            details += f"Target Gender: {program.get('Target Gender', 'N/A')}\n"
            details += f"Duration: {program.get('Time Per Workout', 'N/A')}\n"
            details += f"Days Per Week: {program.get('Days Per Week', 'N/A')}"

            text_widget.insert(tk.END, details)
            text_widget.config(state=tk.DISABLED)  # Make the text read-only

            # Add a scrollbar
            
            text_widget.configure(font=("TkDefaultFont", 10))

            ttk.Button(self.main_frame, text="Get Another Program", command=lambda: self.display_random_program(goal, difficulty, gender)).grid(column=0, row=2, columnspan=2, pady=5)
            ttk.Button(self.main_frame, text="Back to Selection", command=self.create_program_view).grid(column=0, row=3, columnspan=2, pady=5)
            ttk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_view).grid(column=0, row=4, columnspan=2, pady=5)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            print(f"Error in display_random_program: {str(e)}")  # Debug print
            self.create_program_view()
   
   
    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # Placeholder functions for each action
    def select_ingredients(self):
        ingredient = tk.simpledialog.askstring("Input", "Enter an ingredient:")
        if ingredient:
            # Call function to get calories for the ingredient
            messagebox.showinfo("Calories", f"Calories for {ingredient}: X kcal")

    def load_data_view(self):
        self.clear_frame()
        self.master.update()
        ttk.Label(self.main_frame, text="Loading data...", font=("Arial", 16)).grid(column=0, row=0, columnspan=2, pady=10)
        self.data = dataprocessing.Dataprocessing("downloaded")
        self.create_main_view()
    
    def scrape_data_view(self):
        self.clear_frame()
        ttk.Label(self.main_frame, text="Scraping data...", font=("Arial", 16)).grid(column=0, row=0, columnspan=2, pady=10)
        self.data = dataprocessing.Dataprocessing("scrape")
        self.create_main_view()

    def get_workout_movements(self):
        muscle_group = tk.simpledialog.askstring("Input", "Enter muscle group:")
        if muscle_group:
            # Call function to get workout movements recommendations
            messagebox.showinfo("Workout Movements", f"Recommended movements for {muscle_group}: ...")

    def outdoor_activities(self):
        location = simpledialog.askstring("get the weather info", "Enter your location:")
        if location:
            weather_data = weather_api.get_weather(location)
            if weather_data:
                weather_info = self.format_weather_info(weather_data)
                messagebox.showinfo("Weather Information", weather_info)
            else:
                messagebox.showerror("Error", "Unable to retrieve weather data. try another city or check your internet connection.")

    def format_weather_info(self, weather_data):
        location = weather_data['location']
        current = weather_data['current']
        
        info = f"Weather in {location['name']}, {location['country']}:\n"
        info += f"Temperature: {current['temp_c']}°C ({current['temp_f']}°F)\n"
        info += f"Condition: {current['condition']['text']}\n"
        info += f"Humidity: {current['humidity']}%\n"
        info += f"Wind: {current['wind_kph']} km/h, {current['wind_dir']}\n\n"
        
         # Add recommendation based on weather conditions
        if current['temp_c'] < 10:
            info += "It's quite cold outside. Consider indoor activities or dress warmly if going out."
        elif current['temp_c'] > 30:
            info += "It's very hot outside. If exercising outdoors, stay hydrated and avoid peak sun hours."
        elif 'rain' in current['condition']['text'].lower():
            info += "It's raining. Indoor activities are recommended, or bring rain gear if going out."
        else:
            info += "The weather seems suitable for outdoor activities. Enjoy your workout!"
        return info

if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessApp(root)
    root.mainloop()