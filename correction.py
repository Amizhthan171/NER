import pandas as pd

data = {
    'address': {'abc', 1, 857, 800, 600, 500, 95},
    'name': {'def', 2, 123, 456, 789, 100, 80}
}

df = pd.DataFrame(data).transpose().reset_index()
df.columns = ['key', 'value']

df[['address', 'page_no', 'bbox1', 'bbox2', 'bbox3', 'bbox4', 'probability']] = pd.DataFrame(df['value'].tolist())

df = df.drop(columns=['value'])

print(df)
