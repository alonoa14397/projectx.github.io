# controllers/imgbotconfig_controller.py
import os
import json
from app import app

# Function to load imgbotconfig data from JSON file
def load_imgbotconfig():
    imgbotconfig_file = os.path.join(app.config['DATA_FOLDER'], 'imgbotconfig.json')
    with open(imgbotconfig_file, 'r') as f:
        imgbotconfig_data = json.load(f)
    return imgbotconfig_data

# Example function to update imgbotconfig data and save it back to the file
def update_imgbotconfig(new_data):
    imgbotconfig_file = os.path.join(app.config['DATA_FOLDER'], 'imgbotconfig.json')
    with open(imgbotconfig_file, 'w') as f:
        json.dump(new_data, f, indent=4)

# Example function to retrieve specific imgbotconfig information
def get_imgbotconfig_value(key):
    imgbotconfig_data = load_imgbotconfig()
    return imgbotconfig_data.get(key, None)
