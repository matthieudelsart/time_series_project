import pandas as pd
import numpy as np

data_train = pd.read_csv('data/train.csv')
data_test = pd.read_csv('data/test.csv')


def clean_data(data):
    """Transform id column in date format"""
    data['id'] = pd.to_datetime(data['id'])
    return data

def filter_outliers(df):
    """Filter outliers for each column of the train using the IQR (Interquartile Range) method."""
    df_filtered = df.copy()
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df_filtered = df_filtered[(df_filtered[column] >= lower_bound) & (df_filtered[column] <= upper_bound)]
    return df_filtered

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
    # df['Weekday'] = df['id'].dt.weekday
    df['Day'] = df['id'].dt.day
    # df['Hour'] = df['id'].dt.hour
    df['is_weekend'] = (df['id'].dt.weekday >= 5) * 1
    return df

def add_cyclic_datetime_features(df):
    """Add cyclic datetime features to the dataset."""

    df['DayOfYear'] = df['id'].dt.dayofyear
    df['HourOfDay'] = df['id'].dt.hour
    df['Weekday'] = df['id'].dt.weekday

    df['DayOfYear_sin'] = np.sin(2 * np.pi * df['DayOfYear'] / 365)
    df['DayOfYear_cos'] = np.cos(2 * np.pi * df['DayOfYear'] / 365)

    df['HourOfDay_sin'] = np.sin(2 * np.pi * df['HourOfDay'] / 24)
    df['HourOfDay_cos'] = np.cos(2 * np.pi * df['HourOfDay'] / 24)
    
    df['Weekday_sin'] = np.sin(2 * np.pi * df['Weekday'] / 7)
    df['Weekday_cos'] = np.cos(2 * np.pi * df['Weekday'] / 7)

    # df = df.drop(columns=['DayOfYear', 'HourOfDay', 'Weekday'])

    return df

def preprocess_data(data, add_cyclic_features=True, add_filter_outliers=True):
    data = clean_data(data)
    if add_filter_outliers:
        data = filter_outliers(data)
    data = integrate_holidays(data)
    data = integrate_weather(data)
    data = add_datetime_columns(data)
    if add_cyclic_features:
        data = add_cyclic_datetime_features(data)
    return data


#### Submission
def clean_for_submission(data):
    data = data[['id', 'valeur_NO2', 'valeur_CO', 'valeur_O3', 'valeur_PM10', 'valeur_PM25']]
    data['id'] = pd.to_datetime(data['id']).dt.strftime('%Y-%m-%d %H')
    return data
    


if __name__ == "__main__":
    #print(preprocess_data(data_train).head())
    preprocess_data(data_test, add_filter_outliers=False).to_csv('data/test_preprocessed.csv', index=False)