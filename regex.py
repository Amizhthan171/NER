import json
import pandas as pd

def flatten_json(json_obj, parent_key='', separator='_'):
    items = {}
    for key, value in json_obj.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else key
        if isinstance(value, dict):
            items.update(flatten_json(value, new_key, separator))
        else:
            items[new_key] = value
    return items

# Load JSON data from a file or string
with open('data.json', 'r') as json_file:
    json_data = json.load(json_file)

# Flatten JSON
flattened_data = flatten_json(json_data)

# Create a DataFrame
df = pd.DataFrame([flattened_data])

# Convert to CSV
df.to_csv('output.csv', index=False)