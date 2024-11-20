# Predicting air pollutants in Paris

This project was developped for a [Kaggle competition](https://www.kaggle.com/competitions/x-hec-ts-2024-predicting-air-quality-in-paris/overview) on timeseries forecasting. The goal was to predict the hourly concentration of 5 air pollutants in Paris.

Our solution, which allowed our team to rank 1st, leverages external data and relies on 2 models: a Temporal Fusion Transformer and an XGBoost model with lags.

### Table of Contents
1. [Team](#1-team)
2. [Project Presentation](#2-project-presentation)
3. [Our Solution](#3-our-solution)

## 1. Team
Elise Barratini @ebarattini
Benjamin Cerf @benjamincerf57
Matthieu Delsart @matthieudelsart
Augustin de Saint-Affrique @AdeStaff
Malo Renaudin @malo-renaudin
Eva Toledano @eva-toledano

## 2. Project Presentation

Air quality in urban areas is a critical factor affecting the health and well-being of millions. Paris, a bustling metropolis, continuously monitors its air pollutants to safeguard public health and inform policy decisions. In this competition, your challenge is to predict hourly concentrations of five key pollutants—CO, NO₂, O₃, PM10, and PM2.5—over a three-week period using historical data.

This competition is part of a lecture on time series analysis and prediction, offering a practical application of forecasting techniques on real-world environmental data. By accurately predicting pollutant levels, you can contribute to better air quality management and public health initiatives.

Your task is to develop models that forecast the hourly levels of these pollutants based on provided historical measurements. This involves analyzing temporal patterns, trends, and potential seasonal effects within the data to make informed predictions.

Whether you're new to time series analysis or looking to enhance your forecasting skills, this challenge provides an opportunity to engage with meaningful data and address real-world environmental issues!

<details>
  <summary>More details:</summary>
    Air pollutants can have significant impacts on human health and the environment. Below is an overview of the five key pollutants featured in this challenge:<br><br>
    1. Carbon Monoxide (CO)<br>
    Description: Carbon monoxide is a colorless, odorless gas produced by the incomplete combustion of carbon-containing fuels such as gasoline, natural gas, oil, coal, and wood. In urban environments like Paris, the primary sources of CO are vehicle emissions and industrial processes.<br>
    Health Effects: CO binds preferentially to hemoglobin in red blood cells over oxygen, reducing the oxygen-carrying capacity of the blood. Low-level exposure can cause headaches, dizziness, weakness, and nausea, while high-level exposure can be fatal due to oxygen deprivation.<br><br>
    2. Nitrogen Dioxide (NO₂)<br>
    Description: Nitrogen dioxide is a reddish-brown gas with a characteristic sharp, biting odor. It is formed primarily from the combustion of fossil fuels in vehicles, power plants, and industrial facilities.<br>
    Health Effects: NO₂ can irritate airways in the human respiratory system, leading to coughing, wheezing, and difficulty breathing. Long-term exposure can contribute to the development of asthma and increase susceptibility to respiratory infections.<br><br>
    3. Ozone (O₃)<br>
    Description: Ground-level ozone is not emitted directly into the air but is created by chemical reactions between oxides of nitrogen (NOₓ) and volatile organic compounds (VOCs) in the presence of sunlight. Common sources include vehicle exhaust and industrial emissions.<br>
    Health Effects: Ozone can cause chest pain, coughing, throat irritation, and airway inflammation. It can worsen bronchitis, emphysema, and asthma, and reduce lung function, making it difficult to breathe deeply.<br><br>
    4. Particulate Matter 10 (PM10)<br>
    Description: PM10 refers to inhalable particles with diameters that are generally 10 micrometers and smaller. These particles can be found in dust, pollen, mold, and ash, and are often produced by construction sites, unpaved roads, fields, smokestacks, and fires.<br>
    Health Effects: Particles of this size can bypass the nose and throat, entering the lungs. They can cause respiratory issues, aggravate asthma, and lead to decreased lung function and chronic bronchitis.<br><br>
    5. Particulate Matter 2.5 (PM2.5)<br>
    Description: PM2.5 consists of fine inhalable particles with diameters that are generally 2.5 micrometers and smaller. These particles often come from combustion sources such as vehicle engines, power plants, wood burning, and some industrial processes.<br>
    Health Effects: Due to their small size, PM2.5 particles can penetrate deep into the lungs and even enter the bloodstream. Exposure is linked to a variety of health problems, including heart attacks, aggravated asthma, decreased lung function, and premature death in individuals with heart or lung disease.<br><br>
    <b>Evaluation metric:</b><br>
    The average MAE across the 5 pollutants is used as evaluation metric.
</details>

## 3. Our Solution

Our team ranked 1st in the competition. The details of our solution are presented in the **Report.pdf** file.  
It is built upon three main components:
- **Time-series-specific imputation** to fill missing data
- **Curated external data**, particularly meteorological and traffic data.
- **Two separate models**:
  - An XGBoost regressor with lagged features
  - A Temporal Fusion Transformer with significantly fewer features

The detailed investigations and models can be found in the `notebooks` folder.