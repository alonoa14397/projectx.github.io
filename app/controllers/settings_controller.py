# controllers/settings_controller.py
import os
import json
from app import app

# Function to load settings data from JSON file
def load_settings():
    settings_file = os.path.join(app.config['DATA_FOLDER'], 'settings.json')
    with open(settings_file, 'r') as f:
        settings_data = json.load(f)
    return settings_data

# Example function to update settings data and save it back to the file
def update_settings(new_data):
    settings_file = os.path.join(app.config['DATA_FOLDER'], 'settings.json')
    with open(settings_file, 'w') as f:
        json.dump(new_data, f, indent=4)

# Example function to retrieve specific setting value
def get_setting_value(key):
    settings_data = load_settings()
    return settings_data.get(key, None)
