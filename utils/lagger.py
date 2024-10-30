import pandas as pd
import numpy as np

def create_lags(df, columns, max_lag):
    """
    Adds lag columns to a DataFrame for a given list of columns.

    Parameters:
    -----------
    df : pd.DataFrame
        Origine dataframe
    columns : list
        List of columns for which we want to add lags.
    max_lag : int
        Max number of lags to create.

    Returns:
    --------
    pd.DataFrame
        DataFrame lag columns.
    """
    df_lagged = df.copy()
    for col in columns:
        for lag in range(1, max_lag + 1):
            df_lagged[f"{col}_lag_{lag}"] = df[col].shift(lag)
    return df_lagged