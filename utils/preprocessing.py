import pandas as pd
import numpy as np

data_train = pd.read_csv('data/train.csv')
data_test = pd.read_csv('data/test.csv')


def clean_data(data):
    """Transform id column in date format"""
    data['id'] = pd.to_datetime(data['id'])
    return data

def integrate_holidays(data):
    """Integrate holidays data into the main dataset"""
    df_holidays = pd.read_csv(f"external_data/holidays.csv")
    df_holidays = clean_data(df_holidays)
    data = data.merge(df_holidays, how='left', on='id')
    return data

def integrate_weather(data):
    """Integrate weather data into the main dataset."""    
    df_weather = pd.read_csv(f"external_data/weather_clean.csv", parse_dates=['date'])
    data_with_weather = pd.merge(data, df_weather, left_on='id', right_on='date', how='left')
    data_with_weather.drop('date', axis=1, inplace=True)
    return data_with_weather

def add_datetime_columns(df):
    """Integrate datetime columns into the main dataset."""
    df['Year'] = df['id'].dt.year
    df['Month'] = df['id'].dt.month
    df['Weekday'] = df['id'].dt.weekday
    df['Day'] = df['id'].dt.day
    df['Hour'] = df['id'].dt.hour
    df['is_weekend'] = df['id'].dt.weekday >= 5
    return df

def add_cyclic_datetime_features(df):
    """Add cyclic datetime features to the dataset."""

    # Extraction de l'année, jour de l'année et heure
    df['DayOfYear'] = df['id'].dt.dayofyear
    df['HourOfDay'] = df['id'].dt.hour

    # Création des features cycliques
    # Pour le jour de l'année (365 jours dans un cycle)
    df['DayOfYear_sin'] = np.sin(2 * np.pi * df['DayOfYear'] / 365)
    df['DayOfYear_cos'] = np.cos(2 * np.pi * df['DayOfYear'] / 365)
    
    # Pour l'heure de la journée (24 heures dans un cycle)
    df['HourOfDay_sin'] = np.sin(2 * np.pi * df['HourOfDay'] / 24)
    df['HourOfDay_cos'] = np.cos(2 * np.pi * df['HourOfDay'] / 24)
    
    # Optionnel : suppression des colonnes intermédiaires
    df = df.drop(columns=['DayOfYear', 'HourOfDay'])
    
    return df

def preprocess_data(data, add_cyclic_features=True):
    data = clean_data(data)
    data = integrate_holidays(data)
    data = integrate_weather(data)
    data = add_datetime_columns(data)
    if add_cyclic_features:
        data = add_cyclic_datetime_features(data)
    return data

if __name__ == "__main__":
    print(preprocess_data(data_train).head())
