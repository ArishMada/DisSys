import pandas as pd

df = pd.read_csv("AverageQuantityPerMonthPerItem.csv", encoding="windows-1252")
print(df)

df['MeanValue'] = df[['December_2018', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December_2019']].mean(axis=1)

average_quantity_2019 = df[['ProductName', 'MeanValue']].copy()

print(average_quantity_2019)

average_quantity_2019.to_csv('AverageQuantityPerItem2019.csv', index=False)
