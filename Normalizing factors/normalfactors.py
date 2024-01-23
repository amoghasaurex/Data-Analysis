import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_normalfactors = pd.read_csv('normalizing_factors.csv')

df_normalfactors.dropna(inplace=True)

df_pivot3 = df_normalfactors

df_pivot3.plot(kind='line',
               xlabel='Numbers',
               title = 'Normal Factors (2015-2023)')

# save plot
plt.savefig('Normal factors.png')
# show plot
plt.show



