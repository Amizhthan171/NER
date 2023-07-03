import pandas as pd

data = {
    'address': {'abc', 1, 857, 800, 600, 500, 95},
    'name': {'def', 2, 123, 456, 789, 100, 80}
}

df = pd.DataFrame(columns=['KEY', 'VALUE', 'BBOX', 'PAGE NO', 'PROBABILITY'])

for key, value in data.items():
    address = value.pop(0)
    page_no = value.pop(0)
    bbox = value[:4]
    probability = value[-1]
    df = df.append({'KEY': key, 'VALUE': address, 'BBOX': bbox, 'PAGE NO': page_no, 'PROBABILITY': probability}, ignore_index=True)

print(df)