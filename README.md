SmartFitnessManager
Data-Focused Python Course Final Project

Overview
SmartFitnessManager is a Python-based application that focuses on two primary functionalities:

Calorie Tracking – Track your daily caloric intake based on the foods you consume.
Workout Suggestions – Get personalized workout suggestions to help meet your fitness goals.
Features
Calorie Tracking: Input your meals and receive data on calories consumed.
Workout Suggestions: Based on your fitness data, receive workout recommendations tailored to your goals.
Installation Guide
Follow these detailed steps to correctly set up SmartFitnessManager on your local machine:

Prerequisites
Before starting, ensure you have the following installed:

Python 3.7+: You can download it here.
Git: You can download it here.
You can verify Python is installed and check the version by running:

bash
Copy code
python --version
Make sure it is version 3.7 or higher.

1. Clone the Repository
Clone the repository to your local machine using Git:

bash
Copy code
git clone https://github.com/JimmyWu-Peiyuan/SmartFitnessManager.git
2. Navigate to the Project Directory
Move into the project directory:

bash
Copy code
cd SmartFitnessManager
3. (Optional but Strongly Recommended) Create and Activate a Virtual Environment
It is recommended to create a virtual environment to manage dependencies without affecting other projects.

To create a virtual environment:
For Windows, macOS, and Linux:

bash
Copy code
python -m venv venv
Activate the virtual environment:
On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Your command prompt should now show the virtual environment's name, indicating that it's active.

4. Install Required Dependencies
Once the virtual environment is activated, install the required libraries by running:

bash
Copy code
pip install -r requirements.txt
This will install all dependencies listed in requirements.txt.

If requirements.txt Fails:
If the installation fails, try upgrading pip and retry:

bash
Copy code
python -m pip install --upgrade pip
pip install -r requirements.txt
5. Verify the Installation
Once all dependencies are installed, verify that there are no issues by running:

bash
Copy code
pip check
This will ensure all packages are correctly installed and compatible.

6. Running the Application for the First Time
Start the main interface by running:

bash
Copy code
python Interface_Main.py
If any errors occur during runtime (such as missing modules or dependencies), ensure all packages are installed and check the error log for specific issues.

7. Additional Configuration (Optional)
API Keys/Data Resources: If the application requires any API keys or external datasets (as mentioned in the project documentation), make sure you follow the appropriate steps to configure them.
Database Setup: If there's a need to initialize a database, ensure that all migrations or database configuration steps are completed.
8. Deactivating the Virtual Environment
When you're done using the project, deactivate the virtual environment by running:

bash
Copy code
deactivate
9. Updating the Project
To update your local copy of the project, pull the latest changes from the repository:

bash
Copy code
git pull origin main
Usage
Run the main interface:
bash
Copy code
python Interface_Main.py
Follow the on-screen prompts to track calories or get workout suggestions.
Project Structure
DataCollection/: Contains scripts related to collecting fitness and dietary data.
ScrapedData/: Stores pre-scraped data used for processing.
Main Scripts:
Diet_interface_analysis.py: Manages the diet and calorie tracking functionality.
Interface_Main.py: Launches the main application interface.
dataprocessing.py: Handles data manipulation and analysis.
ingredients_analysis.py: Analyzes food ingredients for accurate calorie tracking.
