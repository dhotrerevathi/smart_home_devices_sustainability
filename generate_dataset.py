import pandas as pd
import numpy as np

# Defining distinct device types
device_types = [
    'Lights', 'Thermostat', 'Security System', 'Camera', 'Smart Speaker', 'Smart Lock', 'Smart Plug', 'Smart TV',
    'Smart Refrigerator', 'Smart Oven', 'Smart Microwave', 'Smart Dishwasher', 'Smart Washing Machine', 'Smart Dryer',
    'Smart Vacuum', 'Smart Air Purifier', 'Smart Humidifier', 'Smart Dehumidifier', 'Smart Fan', 'Smart Heater',
    'Smart Air Conditioner', 'Smart Water Heater', 'Smart Sprinkler', 'Smart Doorbell', 'Smart Garage Door Opener',
    'Smart Smoke Detector', 'Smart Carbon Monoxide Detector', 'Smart Light Switch', 'Smart Light Bulb',
    'Smart Security Camera', 'Smart Door Lock', 'Smart Window Sensor', 'Smart Motion Sensor',
    'Smart Leak Sensor', 'Smart Alarm System', 'Smart Pet Feeder', 'Smart Coffee Maker', 'Smart Blender',
    'Smart Toaster', 'Smart Kettle', 'Smart Scale', 'Smart Toothbrush', 'Smart Mirror', 'Smart Bed', 'Smart Pillow',
    'Smart Shower', 'Smart Faucet'
]

# Function to generate data for each device type
def generate_device_data(device_type, num_records):
    user_ids = np.random.randint(0, 1000, num_records)
    usage_hours = np.random.uniform(0.5, 24, num_records)
    energy_consumption = usage_hours * np.random.uniform(0.1, 0.5, num_records)
    user_preferences = np.where(energy_consumption > 5, 1, 0)
    device_age = np.random.randint(1, 60, num_records)
    malfunction_incidents = np.where(device_age > 30, np.random.randint(1, 5, num_records), np.random.randint(0, 2, num_records))
    smart_home_efficiency = np.where((energy_consumption < 5) & (malfunction_incidents < 2), 1, 0)
    
    data = pd.DataFrame({
        'user_id': user_ids,
        'device_type': device_type,
        'usage_hours': usage_hours,
        'energy_consumption': energy_consumption,
        'user_preferences': user_preferences,
        'malfunction_incidents': malfunction_incidents,
        'device_age': device_age,
        'smart_home_efficiency': smart_home_efficiency
    })
    
    return data

# Generate data for all device types
all_data = pd.DataFrame()
for device in device_types:
    device_data = generate_device_data(device, 5000)  # 5000 records per device type
    all_data = pd.concat([all_data, device_data], ignore_index=True)

# Print the head of the dataset
print(all_data.head())

# Save the dataset to a CSV file
all_data.to_csv('smart_home_devices_data.csv', index=False)
print("Dataset generated and saved to 'smart_home_devices_data.csv'")
