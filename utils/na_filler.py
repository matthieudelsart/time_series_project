import numpy as np
import pandas as pd

np.random.seed(1234)

from qolmat.benchmark import comparator, missing_patterns
from qolmat.imputations import imputers
from qolmat.utils import data, plot
from sklearn.linear_model import LinearRegression

def Imputer_MICE(df, columns_to_impute):
    
    imputer_mice = imputers.ImputerMICE(
    estimator=LinearRegression(),
    sample_posterior=False,
    max_iter=100
    )

    df[columns_to_impute] = imputer_mice.fit_transform(df[columns_to_impute])

    return df

def Imputer_TSOU(df, columns_to_impute):

    imputer_tsou = imputers.ImputerEM(
    model="VAR",
    method="mle", 
    max_iter_em=30,
    n_iter_ou=15,
    dt=1e-3,
    p=1)

    df[columns_to_impute] = imputer_tsou.fit_transform(df[columns_to_impute])

    return df
    
