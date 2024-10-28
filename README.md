# time_series_project

## Overview
Overview

Air quality in urban areas is a critical factor affecting the health and well-being of millions. Paris, a bustling metropolis, continuously monitors its air pollutants to safeguard public health and inform policy decisions. In this competition, your challenge is to predict hourly concentrations of five key pollutants—CO, NO₂, O₃, PM10, and PM2.5—over a three-week period using historical data.

This competition is part of an introductory lecture on time series analysis, offering a practical application of forecasting techniques on real-world environmental data. By accurately predicting pollutant levels, you can contribute to better air quality management and public health initiatives.

Your task is to develop models that forecast the hourly levels of these pollutants based on provided historical measurements. This involves analyzing temporal patterns, trends, and potential seasonal effects within the data to make informed predictions.

Whether you're new to time series analysis or looking to enhance your forecasting skills, this challenge provides an opportunity to engage with meaningful data and address real-world environmental issues!


Air pollutants can have significant impacts on human health and the environment. Below is an overview of the five key pollutants featured in this challenge:

1. Carbon Monoxide (CO)

Description: Carbon monoxide is a colorless, odorless gas produced by the incomplete combustion of carbon-containing fuels such as gasoline, natural gas, oil, coal, and wood. In urban environments like Paris, the primary sources of CO are vehicle emissions and industrial processes.

Health Effects: CO binds preferentially to hemoglobin in red blood cells over oxygen, reducing the oxygen-carrying capacity of the blood. Low-level exposure can cause headaches, dizziness, weakness, and nausea, while high-level exposure can be fatal due to oxygen deprivation.

2. Nitrogen Dioxide (NO₂)

Description: Nitrogen dioxide is a reddish-brown gas with a characteristic sharp, biting odor. It is formed primarily from the combustion of fossil fuels in vehicles, power plants, and industrial facilities.

Health Effects: NO₂ can irritate airways in the human respiratory system, leading to coughing, wheezing, and difficulty breathing. Long-term exposure can contribute to the development of asthma and increase susceptibility to respiratory infections.

3. Ozone (O₃)

Description: Ground-level ozone is not emitted directly into the air but is created by chemical reactions between oxides of nitrogen (NOₓ) and volatile organic compounds (VOCs) in the presence of sunlight. Common sources include vehicle exhaust and industrial emissions.

Health Effects: Ozone can cause chest pain, coughing, throat irritation, and airway inflammation. It can worsen bronchitis, emphysema, and asthma, and reduce lung function, making it difficult to breathe deeply.

4. Particulate Matter 10 (PM10)

Description: PM10 refers to inhalable particles with diameters that are generally 10 micrometers and smaller. These particles can be found in dust, pollen, mold, and ash, and are often produced by construction sites, unpaved roads, fields, smokestacks, and fires.

Health Effects: Particles of this size can bypass the nose and throat, entering the lungs. They can cause respiratory issues, aggravate asthma, and lead to decreased lung function and chronic bronchitis.

5. Particulate Matter 2.5 (PM2.5)

Description: PM2.5 consists of fine inhalable particles with diameters that are generally 2.5 micrometers and smaller. These particles often come from combustion sources such as vehicle engines, power plants, wood burning, and some industrial processes.

Health Effects: Due to their small size, PM2.5 particles can penetrate deep into the lungs and even enter the bloodstream. Exposure is linked to a variety of health problems, including heart attacks, aggravated asthma, decreased lung function, and premature death in individuals with heart or lung disease.

## Use of External Data

Participants are encouraged to enhance their models by incorporating external data sources beyond the provided dataset. Utilizing additional information can improve the accuracy of your predictions and provide deeper insights into the factors affecting air quality.

### Allowed External Data

1. Weather Data

You may use historical and forecasted weather data to assist in predicting pollutant levels. Weather conditions such as temperature, humidity, wind speed, and atmospheric pressure can significantly influence air quality. For the purpose of this competition:

- Past Weather Data: You can use historical weather data corresponding to the training period.
- Future Weather Data (Test Period): You are allowed to use weather data for the test period as if it were perfectly predicted. This means you can include weather variables for the time frames you are forecasting without penalty.

Example Sources:

- National meteorological services
- Weather APIs (e.g., OpenWeatherMap, Weather Underground)
- Climatological datasets from reputable organizations

2. Public Holidays and Events

Including information about public holidays, festivals, or significant events can be beneficial, as such occasions may influence pollution levels due to changes in traffic patterns and industrial activity.

Example Sources:

- Official government calendars
- Event listings and schedules

3. Traffic Data

Traffic density and patterns can affect emissions, particularly in urban areas. You may include historical traffic data if available.

Example Sources:

- City traffic reports
- Transportation department datasets

### Restrictions on External Data

- Measurement-Time Data: You should not use any external data that provides direct measurements or observations of pollutant levels during the test period beyond what is provided in the dataset.
- Real-Time Pollutant Data: Avoid using any live or real-time air quality monitoring data for the test period.
- Proprietary Data: Ensure that any external data used is publicly available and does not violate any copyright or usage rights.

### Citing External Data Sources

When using external data, please document and cite all sources appropriately in your submission. This transparency helps in verifying the legality and relevance of the data used.

### Why Use External Data?

Incorporating external data can help capture variables that influence air quality but are not included in the provided dataset. For instance:

- Weather conditions affect pollutant dispersion and chemical reactions in the atmosphere.
- Human activities such as traffic volume and industrial operations can vary based on the day of the week or special events.
- Seasonal patterns may influence heating requirements and consequently, emission levels.

By thoughtfully integrating external data, you can develop more robust models that generalize better to unseen data.
## Evaluation

### Evaluation Metric

Your submissions will be evaluated using the Mean Absolute Error (MAE) between your predicted pollutant levels and the actual observed values over the test period.
Mean Absolute Error (MAE)

### Definition:

The Mean Absolute Error measures the average magnitude of errors in a set of predictions, without considering their direction. It is calculated as the average of the absolute differences between the predicted and actual values.

Formula:

MAE = (1/n) * Σ | y_i - ŷ_i |

where:

- n is the number of observations.
- y_i is the actual value at time i.
- ŷ_i (y_hat_i) is the predicted value at time i.
- Σ denotes the summation over all observations.

### Final Score Calculation

The MAE will be calculated separately for each of the five pollutants. Your overall score will be the average of these five MAE values.

Final Score Formula:

Final Score = (1/5) * Σ MAE_p

where:

- MAE_p is the Mean Absolute Error for pollutant p.
- The summation Σ runs over all five pollutants (CO, NO₂, O₃, PM10, and PM2.5).

### Evaluation Details

- Per-Pollutant Calculation: The MAE is computed individually for each pollutant to ensure balanced performance across all pollutants.
- Equal Weighting: Each pollutant contributes equally (20%) to the final score.
- Time Frame: Predictions are required for every hour over the three-week test period.
- Submission Format: Ensure your submission follows the specified format to be correctly evaluated.

### Interpretation

- Lower MAE Values: Indicate better predictive accuracy and model performance.
- Consistency Across Pollutants: Consistent performance across all pollutants is crucial due to equal weighting.

### Tips for Improving MAE

- Data Preprocessing: Address missing values and outliers to improve data quality.
- Feature Engineering: Incorporate relevant external features like weather data and public events.
- Model Selection: Try different models suited for time series forecasting, such as ARIMA, Prophet, or LSTM networks.
- Validation Strategy: Use cross-validation methods appropriate for time series data, like time-based splitting.

### Missing values in the test dataset

If there is missing values in the test dataset, they have been filled using the approach with the best MAE score obtained using the QOLMAT library.

## Leaderboard
### Public Leaderboard

- Score Calculation: During the competition, the public leaderboard will display scores calculated using your predictions for the first week of the test period.
- Purpose: This allows you to monitor your model's initial performance and compare it with others without revealing full test results.
- Updates: The leaderboard will update with each valid submission, reflecting your latest score based on the first week's data.

### Final Evaluation

- Final Score Calculation: After the competition ends, your final score will be calculated using your predictions for the entire three-week test period.
- Final Rankings: The final rankings may differ from the public leaderboard standings due to performance over the remaining two weeks.
- Objective: This approach encourages the development of models that generalize well over the entire forecast horizon, not just the initial period.

### The Baseline

The baseline value was obtained by predicting the average value for all polluants on the training dataset, for all time steps.


## Data
### Files

- train.csv - the training set, use this file to train your model. You can enriched it with external data and perform feature engineering.
- test.csv - the test set, list of time step that you need to predict.
- sample_submission.csv - a sample submission file in the correct format, keep the same table format (columns names) and do not change the id column for your submission (just modify the valeur_CO, valeur_NO2, valeur_O3, valeur_PM10, valeur_PM25)

### Columns

- id: The date and time of the measurement, in Central European Time (CET).
- valeur_CO: Measured concentration of Carbon Monoxide in milligrams per cubic meter (mg/m³).
- valeur_NO2: Measured concentration of Nitrogen Dioxide in micrograms per cubic meter (µg/m³).
- valeur_O3: Measured concentration of Ozone in micrograms per cubic meter (µg/m³).
- valeur_PM10: Measured concentration of Particulate Matter 10 micrometers or less in diameter in micrograms per cubic meter (µg/m³).
- valeur_PM25: Measured concentration of Particulate Matter 2.5 micrometers or less in diameter in micrograms per cubic meter (µg/m³).
