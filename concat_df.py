import pandas as pd

data = {
    'customerKey': [1, 2, 1, 4, 4],
    'MessageName': ['Message 1', 'Message 2', 'Message 3', 'Message 4', 'Message 5'],
    'Action': ['delivered', 'open', 'open', 'open', 'delivered']
}
df = pd.DataFrame(data)
df_sorted = df.sort_values(by=['customerKey', 'Action'])
grouped = df_sorted.groupby('customerKey')
df_concatenated = grouped['Action'].apply(lambda x: ', '.join(x)).reset_index()
df_merged = pd.merge(df, df_concatenated, on='customerKey')
df_unique = df_merged[df_merged['Action_x'] == 'open'].drop_duplicates(subset=['customerKey'])
df_unique.drop('Action_x', axis=1, inplace=True)
df_unique.rename(columns={'Action_y': 'Action'}, inplace=True)
print(df_unique)
