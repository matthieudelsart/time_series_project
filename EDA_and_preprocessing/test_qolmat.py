import time
start_time = time.time()

import numpy as np
import pandas as pd
from utils.na_filler import Imputer_TSOU

df = pd.read_csv('data/train.csv')

df['id'] = pd.to_datetime(df['id'])
df.set_index('id', inplace=True)

cols_to_impute = ["valeur_NO2", "valeur_CO", "valeur_O3", "valeur_PM10", "valeur_PM25"]

print(cols_to_impute)

df = df.iloc[:1000] # Number of rows to test
df = Imputer_TSOU(df, cols_to_impute)

print(df.isna().sum())

end_time = time.time()
print("Temps d'exécution : {:.2f} secondes".format(end_time - start_time))
