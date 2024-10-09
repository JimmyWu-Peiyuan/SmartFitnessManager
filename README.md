# SmartFitnessManager

**Data Focused Python Course Final Project**

## Overview

SmartFitnessManager is a Python-based application that focuses on two primary functionalities:
1. **Calories Tracking** - Track your daily caloric intake based on the foods you consume.
2. **Workout Suggestions** - Get personalized workout suggestions to help meet your fitness goals.

## Features

- **Calories Tracking**: Input your meals and receive data on calories consumed.
- **Workout Suggestions**: Based on your fitness data, receive workout recommendations tailored to your goals.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/JimmyWu-Peiyuan/SmartFitnessManager.git
    ```
2. Navigate to the project directory:
    ```bash
    cd SmartFitnessManager
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the main interface:
    ```bash
    python Interface_Main.py
    ```
2. Follow the on-screen prompts to track calories or get workout suggestions.

## Project Structure

- `DataCollection/`: Contains scripts related to collecting fitness and dietary data.
- `ScrapedData/`: Stores pre-scraped data used for processing.
- Main scripts:
  - `Diet_interface_analysis.py`: Manages the diet and calorie tracking functionality.
  - `Interface_Main.py`: Launches the main application interface.
  - `dataprocessing.py`: Handles data manipulation and analysis.
  - `ingredients_analysis.py`: Analyses food ingredients for calorie tracking.
