# SECFC: Survey Embedded Carbon Footprint Calculator

The SECFC (Survey Embedded Carbon Footprint Calculator) is a Python package designed to calculate the carbon footprint of individuals based on their survey responses. This tutorial will guide you through using the package to calculate carbon footprints from survey data.

## Installation

To use SECFC, ensure you have the following dependencies installed:
- pandas
- numpy
- matplotlib (optional, for plotting)

```python
pip install pandas numpy matplotlib
```

## Using SECFC
### Step 1: Import the Package
Begin by importing the necessary functions from SECFC.

```python
import pandas as pd
import numpy as np
from secfc import (
    calculate_personal_emissions,
    calculate_food_emissions,
    calculate_housing_emissions,
    calculate_consumption_emissions,
    calculate_all_emissions
)
```

### Step 2: Prepare Your Survey Data
Ensure your survey data is in a pandas DataFrame format (if you are using the Qualtrics template we provided, please ensure that the variable name are consistent). The columns should match the expected survey questions, as shown in the template below:

```python
C1_Car_Usage, C2_Car_type, C3_Travel_Distance, C4_Public_Transport, Q74, C5_Air_Travel, C4_Public_Transport2, F3_Q28_1, F3_Q28_2, F3_Q28_3, F3_Q28_4, E2_Electricity_bill_1, E3_natural_gas_bill_1, US_Zip_Code, Q84_1, Q84_2, Q84_4, Q84_5, Q84_6, Q84_7, Q84_8, CL1_Q31, Family_size_6, Family_size_14, Family_size_15
```

### Step 3: Calculate Emissions
#### Transport Emissions
Calculate the carbon footprint from transportation.

```python

df = pd.read_csv('data.csv')
df = calculate_personal_emissions(df)
```

#### Food Emissions
Calculate the carbon footprint from food consumption.

```python

df = calculate_food_emissions(df)
```

#### Housing Emissions
Calculate the carbon footprint from housing.

```python

df = calculate_housing_emissions(df)

```

#### Consumption Emissions
Calculate the carbon footprint from living consumption.

```python
df = calculate_consumption_emissions(df)

```

### Step 4: Calculate Total Emissions

Combine all calculated emissions to get the total carbon footprint. Optionally, you can plot the distribution of total emissions.

```python
df = calculate_all_emissions(df, plot=True)
```

### Example Usage
Below is a complete example demonstrating how to load your data and calculate the total carbon footprint:

```python
import pandas as pd

# Load your survey data
df = pd.read_csv('data.csv')

# Calculate emissions from various categories
df = calculate_personal_emissions(df)
df = calculate_food_emissions(df)
df = calculate_housing_emissions(df)
df = calculate_consumption_emissions(df)

# Calculate total emissions and plot the distribution
df = calculate_all_emissions(df, plot=True)

# Display the first few rows of the dataframe
print(df.head())
```

### Survey Template (provided in this repo)
Ensure your survey data is structured as follows:


C1_Car_Usage: Number of days per week using a car
C2_Car_type: Type of car used (1: Electric, 2: Hybrid, 3: Gasoline, 4: Diesel, 5: Natural gas)
C3_Travel_Distance: Code for travel distance per day (1: <5km, 2: 5-10km, 3: 10-30km, 4: >30km)
C4_Public_Transport: Frequency of public transport use (1: Daily, 2: Weekly, 3: Monthly, 4: Rarely, 5: Never)
Q74: Code for public transport travel distance per day (1: <5km, 2: 5-10km, 3: 10-30km, 4: >30km)
C5_Air_Travel: Number of flights per year
C4_Public_Transport2: Frequency of long-distance train use (1: Daily, 2: Weekly, 3: Monthly, 4: Rarely, 5: Never)
F3_Q28_1: Number of meat-based meals per week
F3_Q28_2: Number of vegan meals per week
F3_Q28_3: Number of vegetarian meals per week
F3_Q28_4: Number of dairy products consumed per week (liters)
E2_Electricity_bill_1: Monthly electricity bill (USD)
E3_natural_gas_bill_1: Monthly natural gas bill (USD)
US_Zip_Code: Zip code for location classification
Q84_1: Monthly spending on food delivery (USD)
Q84_2: Monthly spending on dining out (USD)
Q84_4: Monthly spending on hotel stays (USD)
Q84_5: Monthly spending on tobacco products (USD)
Q84_6: Monthly spending on alcoholic drinks (USD)
Q84_7: Monthly spending on entertainment (USD)
Q84_8: Monthly spending on healthcare (USD)
CL1_Q31: Annual spending on clothing (1: >600, 2: 420-600, 3: 300-420, 4: 120-300, 5: <120)
Family_size_6, Family_size_14, Family_size_15: Family size categories for calculating per capita emissions



