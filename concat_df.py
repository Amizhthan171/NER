import pandas as pd

data = {
    'customerKey': [1, 2, 1, 4, 4],
    'MessageName': ['Message 1', 'Message 2', 'Message 1', 'Message 4', 'Message 5'],
    'Action': ['open', 'open', 'delivered', 'open', 'delivered']
}
df = pd.DataFrame(data)
df_sorted = df.sort_values(by=['customerKey', 'Action'])
grouped = df_sorted.groupby('customerKey')
df_concatenated = grouped['Action'].apply(lambda x: ', '.join(x)).reset_index()
df_merged = pd.merge(df, df_concatenated, on='customerKey')
df_unique = df_merged.drop_duplicates(subset=['customerKey'])
print(df_unique)
