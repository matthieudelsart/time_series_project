import pandas as pd
from sklearn.pipeline import Pipeline

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

def preprocess_data(data):
    data = clean_data(data)
    data = integrate_holidays(data)
    data = integrate_weather(data)
    return data