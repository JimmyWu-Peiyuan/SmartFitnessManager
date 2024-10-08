import pandas as pd
import numpy as np
from DataCollection import scrape_athome_program, scrape_fatloss_program,scrape_ingredients,scrape_muscle_program
class Dataprocessing:

    def __init__(self, choice):
        if choice == "scrape":
            self.athome_program = scrape_athome_program.scrape_athome_programs()
            self.fatloss_program = scrape_fatloss_program.scrape_fat_loss_programs()
            self.musclebuilding_program = scrape_muscle_program.scrape_muscle_programs()
            self.ingredients = scrape_ingredients.scrape_ingredients()
        else:
            self.athome_program = pd.read_csv("ScrapedData/athome_programs.csv")
            self.fatloss_program = pd.read_csv("ScrapedData/fatloss_programs.csv")
            self.musclebuilding_program = pd.read_csv("ScrapedData/muscle_programs.csv")
            self.ingredients = pd.read_csv("ScrapedData/ingredients.csv")


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


