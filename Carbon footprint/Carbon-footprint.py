import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1 Creating a DataFrame from a csv file

## 1.1 Carbon footprint

# reading the csv file
df_carbon = pd.read_csv('carbon_footprint_by_product.csv')

df_pivot = df_carbon

df_pivot= df_pivot

df_pivot.plot(kind='line',
              xlabel='Time',
              ylabel='Label',
              title='Carbon Footprint (2015-2022)')

#save plot
plt.savefig('Carbon Footprint')
#show plot
plt.show()

df_pivot.to_excel('Carbon_foorprint.xlsx')

