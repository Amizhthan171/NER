import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({'Document Type': ['Type A', 'Type B', 'Type A', 'Type B'],
                   'Value': [10, 20, 30, 40]})

# Create an Excel writer
writer = pd.ExcelWriter('grouped_data.xlsx', engine='xlsxwriter')

# Group the dataframe by 'Document Type'
grouped = df.groupby('Document Type')

# Iterate over the groups and save each as a separate sheet
for name, group in grouped:
    group.to_excel(writer, sheet_name=name, index=False)

# Save the Excel file
writer.save()