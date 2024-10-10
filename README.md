# SmartFitnessManager

**Data-Focused Python Course Final Project**

## Overview
SmartFitnessManager is a Python-based application that focuses on two primary functionalities:

1. **Calorie Tracking** – Track your daily caloric intake based on the foods you consume.
2. **Workout Suggestions** – Get personalized workout suggestions to help meet your fitness goals.

## Features

- **Calorie Tracking**: Input your meals and receive data on calories consumed.
- **Workout Suggestions**: Based on your fitness data, receive workout recommendations tailored to your goals.

## Installation Guide
Follow these detailed steps to correctly set up **SmartFitnessManager** on your local machine:

### Prerequisites
Before starting, ensure you have the following installed:

- **Python 3.7+**: You can download it [here](https://www.python.org/downloads/).
- **Git**: You can download it [here](https://git-scm.com/).

You can verify Python is installed and check the version by running:
```bash
python --version
```
Make sure it is version 3.7 or higher.

### 1. Clone the Repository
Clone the repository to your local machine using Git:
```bash
git clone https://github.com/JimmyWu-Peiyuan/SmartFitnessManager.git
```

### 2. Navigate to the Project Directory
Move into the project directory:
```bash
cd SmartFitnessManager
```

### 3. (Optional but Strongly Recommended) Create and Activate a Virtual Environment
It is recommended to create a virtual environment to manage dependencies without affecting other projects.

#### To create a virtual environment:
For **Windows**, **macOS**, and **Linux**:
```bash
python -m venv venv
```

#### Activate the virtual environment:
- On **Windows**:
    ```bash
    venv\Scripts\activate
    ```
- On **macOS/Linux**:
    ```bash
    source venv/bin/activate
    ```

Your command prompt should now show the virtual environment's name, indicating that it's active.

### 5. Running the Application for the First Time
Start the main interface by running:
```bash
python Interface_Main.py
```

If any errors occur during runtime (such as missing modules or dependencies), ensure all packages are installed and check the error log for specific issues.

### 6. Deactivating the Virtual Environment
When you're done using the project, deactivate the virtual environment by running:
```bash
deactivate
```

### 7. Updating the Project
To update your local copy of the project, pull the latest changes from the repository:
```bash
git pull origin main
```

---

## Usage

1. Run the main interface:
    ```bash
    python Interface_Main.py
    ```
2. Follow the on-screen prompts to track calories or get workout suggestions.

## Project Structure

- `DataCollection/`: Contains scripts related to collecting fitness and dietary data.
- `ScrapedData/`: Stores pre-scraped data used for processing.

### Main Scripts:
- **`Diet_interface_analysis.py`**: Manages the diet and calorie tracking functionality.
- **`Interface_Main.py`**: Launches the main application interface.
- **`dataprocessing.py`**: Handles data manipulation and analysis.
- **`ingredients_analysis.py`**: Analyzes food ingredients for accurate calorie tracking.
