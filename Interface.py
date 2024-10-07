import tkinter as tk
from tkinter import ttk, messagebox,simpledialog
from DataCollection import weather_api 
import pandas as pd


class FitnessApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Fitness Tracker")
        self.master.geometry("500x400")
        self.main_frame = ttk.Frame(self.master, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.ingredients = None
        self.fatloss_programs = None
        self.muscle_programs = None
        self.movements = None
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
        ttk.Label(self.main_frame, text="Calories Tracker", font=("Arial", 16)).grid(column=0, row=0, columnspan=2, pady=10)
        ttk.Button(self.main_frame, text="Select Ingredients", command=self.select_ingredients).grid(column=0, row=1, pady=5, padx=5, sticky=tk.W+tk.E)
        ttk.Button(self.main_frame, text="Use Existing Data Source", command=self.use_existing_data).grid(column=0, row=2, pady=5, padx=5, sticky=tk.W+tk.E)
        ttk.Button(self.main_frame, text="Scrape New Data Source", command=self.scrape_new_data).grid(column=0, row=3, pady=5, padx=5, sticky=tk.W+tk.E)
        ttk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_view).grid(column=0, row=4, pady=5, padx=5, sticky=tk.W+tk.E)

    def create_workout_view(self):
        self.clear_frame()
        ttk.Label(self.main_frame, text="Select the Type of Workout", font=("Arial", 16)).grid(column=0, row=0, columnspan=2, pady=10)
        ttk.Button(self.main_frame, text="Get Workout Program", command=self.get_workout_program).grid(column=0, row=1, pady=5, padx=5, sticky=tk.W+tk.E)
        ttk.Button(self.main_frame, text="Get Workout Movements", command=self.get_workout_movements).grid(column=0, row=2, pady=5, padx=5, sticky=tk.W+tk.E)
        ttk.Button(self.main_frame, text="Outdoor Activities", command=self.outdoor_activities).grid(column=0, row=3, pady=5, padx=5, sticky=tk.W+tk.E)
        ttk.Button(self.main_frame, text="Back to Main Menu", command=self.create_main_view).grid(column=0, row=4, pady=5, padx=5, sticky=tk.W+tk.E)

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
        try:
            self.ingredients = pd.read_csv('SourceData/ingredients.csv')
            messagebox.showinfo("Success", "Data loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {str(e)}")
        print("need more work done")
        self.create_main_view()
    
    def scrape_data_view(self):
        self.clear_frame()
        ttk.Label(self.main_frame, text="Scraping data...", font=("Arial", 16)).grid(column=0, row=0, columnspan=2, pady=10)
        print("need more work done")
        self.create_main_view()

    def use_existing_data(self):
        messagebox.showinfo("Info", "Using existing data source...")

    def scrape_new_data(self):
        messagebox.showinfo("Info", "Scraping new data source...")

    def get_workout_program(self):
        goal = tk.simpledialog.askstring("Input", "Select goal (fat_loss/muscle_building/at_home):")
        difficulty = tk.simpledialog.askstring("Input", "Select difficulty (easy/medium/hard):")
        if goal and difficulty:
            # Call function to get workout program recommendations
            messagebox.showinfo("Workout Program", f"Workout program for {goal} at {difficulty} difficulty: ...")

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