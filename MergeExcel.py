import pandas as pd

# Read data from the two Excel files (replace 'file1.xlsx' and 'file2.xlsx' with the actual file names)
df1 = pd.read_excel('Marks Outof 100.xlsx')  # Assuming the first dataset is in 'file1.xlsx'
df2 = pd.read_excel('Marks Outof 40.xlsx')  # Assuming the second dataset is in 'file2.xlsx'

# Merge the two datasets based on the 'Subject' column
merged_df = pd.merge(df1, df2, on='Subject')

# Display the merged DataFrame
print(merged_df)

# Optionally, you can save the merged DataFrame to a new Excel file
merged_df.to_excel('merged_output.xlsx', index=False)
