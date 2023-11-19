import pandas as pd

df = pd.read_csv("Sales Transactions 1.csv", encoding = "windows-1252")
print(df)

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Filter data for the year 2019
df_2019 = df[df['Date'].dt.year == 2019]

# Calculate the average quantity sold per item for the year 2019
average_quantity_2019 = df_2019.groupby('ProductName')['Quantity'].mean().reset_index()

average_quantity_2019['Quantity'] = average_quantity_2019['Quantity'].round(3)
average_quantity_2019 = average_quantity_2019.rename(columns={'Quantity': 'QuantityPerYear'})

# Print or display the result
print(average_quantity_2019)

average_quantity_2019 = average_quantity_2019.fillna(0)

average_quantity_2019.to_csv('AverageQuantityPerItem2019.csv', index=False)