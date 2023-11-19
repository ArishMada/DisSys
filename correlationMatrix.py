import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

data=pd.read_csv("inventory1.csv")
print(data.head())

print(data.columns)

data_scaled = data.iloc[:, 1:]

#now plot correlation matrix
correl=data_scaled.corr()
ax=plt.subplots(figsize=(15,9))
sns.heatmap(correl,vmax=0.8,square=True)

plt.show()