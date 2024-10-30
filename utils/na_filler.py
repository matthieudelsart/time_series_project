import numpy as np
import pandas as pd

np.random.seed(1234)

from qolmat.benchmark import comparator, missing_patterns
from qolmat.imputations import imputers
from qolmat.utils import data, plot
from sklearn.linear_model import LinearRegression

def Imputer_MICE(df, columns_to_impute, nb_days=None):
        
    if nb_days is None:
        nb_transform = df.shape[0]
    else:
        nb_transform = nb_days*24

    df = df.tail(nb_transform)

    # Filtre les colonnes pour ne garder que celles numériques
    df_numeric = df[columns_to_impute].select_dtypes(include=[np.number])


    imputer_mice = imputers.ImputerMICE(
    estimator=LinearRegression(),
    sample_posterior=False,
    max_iter=100
    )

    imputer_mice.fit(df_numeric)
    df[columns_to_impute] = imputer_mice.transform(df[columns_to_impute])

    return df

def Imputer_TSOU(df, columns_to_impute, nb_days=None):
    
    if nb_days is None:
        nb_transform = df.shape[0]
    else:
        nb_transform = nb_days*24

    df = df.tail(nb_transform)

    # Filtre les colonnes pour ne garder que celles numériques
    df_numeric = df[columns_to_impute].select_dtypes(include=[np.number])

    imputer_tsou = imputers.ImputerEM(
    model="VAR",
    method="mle", 
    max_iter_em=30,
    n_iter_ou=15,
    dt=1e-3,
    p=1)

    imputer_tsou.fit(df_numeric)
    df[columns_to_impute] = imputer_tsou.transform(df[columns_to_impute])

    return df
    
