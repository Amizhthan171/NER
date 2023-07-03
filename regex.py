import pandas as pd

data = {
    'address': ['abc', 1, 800, 8000, 800, 800, 90],
    'name': ['def', 2, 123, 456, 789, 100, 80]
}

df = pd.DataFrame(columns=['KEY', 'VALUE', 'BBOX', 'PAGE NO', 'PROBABILITY'])

for key, value in data.items():
    address = value[0]
    bbox = value[2:6]
    page_no = value[1]
    probability = value[6]
    df = df.append({'KEY': key, 'VALUE': address, 'BBOX': bbox, 'PAGE NO': page_no, 'PROBABILITY': probability}, ignore_index=True)

print(df)