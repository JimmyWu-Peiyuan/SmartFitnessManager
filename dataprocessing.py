import pandas as pd
import numpy as np
from DataCollection import scrape_athome_program, scrape_fatloss_program,scrape_ingredients,scrape_muscle_program
class Dataprocessing:


    # some codes use ChatGPT
    def __init__(self, choice):
        if choice == "scrape":
            self.athome_program = scrape_athome_program.scrape_athome_programs()
            self.fatloss_program = scrape_fatloss_program.scrape_fat_loss_programs()
            self.musclebuilding_program = scrape_muscle_program.scrape_muscle_programs()
            self.ingredients = scrape_ingredients.scrape_ingredients()
            self.movements = pd.read_csv("ScrapedData/workout_movements.csv")
        else:
            self.athome_program = pd.read_csv("ScrapedData/athome_programs.csv")
            self.fatloss_program = pd.read_csv("ScrapedData/fatloss_programs.csv")
            self.musclebuilding_program = pd.read_csv("ScrapedData/muscle_programs.csv")
            self.ingredients = pd.read_csv("ScrapedData/ingredients.csv")
            self.movements = pd.read_csv("ScrapedData/workout_movements.csv")
            self.add_equipment_type()

    def getPrograms(self, selection, training_level, gender):
        if selection == "athome":
            df = self.athome_program
        elif selection == "fatloss":
            df = self.fatloss_program
        elif selection == "musclebuilding":
            df = self.musclebuilding_program
        else:
            return None  
        matched = df[df["Training Level"] == training_level]
        if gender.lower() == "male":
            matched = matched[matched["Target Gender"].isin(["Male & Female", "Male"])]
        elif gender.lower() == "female":
            matched = matched[matched["Target Gender"].isin(["Male & Female", "Female"])]
        
        return matched.to_dict("records")

    def add_equipment_type(self):
            # Define equipment keywords
            equipment_keywords = ['barbell', 'dumbbell', 'machine', 'cable']

            # Add new 'equipment' column
            self.movements['equipment'] = 'other'
            
            for keyword in equipment_keywords:
                mask = self.movements['title'].str.contains(keyword, case=False)
                self.movements.loc[mask, 'equipment'] = keyword

    def getMovements(self, muscle_group, equipment_type):
        # Filter by muscle group
        muscle_mask = self.movements['body'].str.contains(muscle_group, case=False, na=False)
        filtered_movements = self.movements[muscle_mask]

        if equipment_type.lower() != 'any':
            equipment_mask = filtered_movements['equipment'] == equipment_type
            filtered_movements = filtered_movements[equipment_mask]

        return filtered_movements.to_dict('records')


    

dp = Dataprocessing("download")
print(dp.movements["equipment"])