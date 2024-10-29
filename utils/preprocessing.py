import numpy as np
import pandas as pd

np.random.seed(1234)

from qolmat.benchmark import comparator, missing_patterns
from qolmat.imputations import imputers
from qolmat.utils import data, plot
from sklearn.linear_model import LinearRegression

def Imputer_MICE(df):
    
    imputer_mice = imputers.ImputerMICE(
    estimator=LinearRegression(),
    sample_posterior=False,
    max_iter=100
    )

    df_imputed = imputer_mice.fit_transform(df)

    return df_imputed

def Imputer_TSOU(df):

    imputer_tsou = imputers.ImputerEM(
    model="VAR",
    method="mle", # Check if we take mle or sample
    max_iter_em=30,
    n_iter_ou=15,
    dt=1e-3,
    p=1)

    df_imputed = imputer_tsou.fit_transform(df)

    return df_imputed
    
