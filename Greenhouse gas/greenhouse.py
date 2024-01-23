import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt

# 2 creating a DataFrame readin the csv file

## 2.2 Green house emission

# reading the csv file
df_greenhouse = pd.read_csv('greenhouse_emissions.csv')

df_pivot2 = df_greenhouse

df_pivot2 = df_pivot2

df_pivot2.plot(kind ='line',
               xlabel='Time',
               ylabel='Metric',
               title='Greenhouse (2015-2022)')

# Save plot
plt.savefig('Greenhouse')
# Show plot
plt.show()

