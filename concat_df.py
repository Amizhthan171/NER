import tabula

# Replace "path/to/your/table.pdf" with the path to your PDF file
# Pass the pages parameter to specify the page number(s) with the table(s) you want to extract
# You can also pass the area parameter to specify the region of the page where the table is located (format: [top, left, bottom, right])
tables = tabula.read_pdf("path/to/your/table.pdf", pages="all")

# Iterate through the extracted tables and display them
for idx, table_df in enumerate(tables):
    print(f"Table {idx + 1}:")
    print(table_df)
    print("\n")  # Add a newline between tables

# Note:⬤