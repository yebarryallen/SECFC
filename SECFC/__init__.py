import pandas as pd
import numpy as np
################# Transport Carbon Footprint Calculation ################

def calculate_personal_emissions(df, emission_factors=None):
    if emission_factors is None:
        emission_factors = {
            "Gasoline Vehicles": 0.14748,  # kg CO2 per km
            "Diesel Vehicles": 0.16327,    # kg CO2 per km
            "Electric Vehicles": 0.0,      # kg CO2 per km (assumed to be zero)
            "Hybrid Vehicles": 0.07374,    # kg CO2 per km (assumed to be half of gasoline)
            "Natural gas Vehicles": 0.1279,  # kg CO2 per km
            "Public Transport": 0.018949,  # kg CO2 per km
            "Flights": 1.05285,            # kg CO2 per km
            "Long Distance Train": 0.039489129  # kg CO2 per km
        }

    # Function to calculate weekly travel distance based on survey responses
    def calculate_weekly_distance(days, distance_code):
        if pd.isna(days) or pd.isna(distance_code):
            return 0
        distance_values = [5, 10, 30.5, 51]  # Approximate midpoint values for distance ranges
        distance_per_day = distance_values[distance_code - 1]
        return days * distance_per_day

    # Map car type to emission factor
    def map_car_type(car_type_code):
        car_types = ["Electric Vehicles", "Hybrid Vehicles", "Gasoline Vehicles", "Diesel Vehicles", "Natural gas Vehicles"]
        if pd.isna(car_type_code):
            return np.nan
        return car_types[car_type_code - 1]

    # Map public transport frequency to usage factor
    def map_public_transport_usage(frequency_code):
        usage_factors = [1, 1/7, 1/30, 1/90, 0]  # Daily, Weekly, Monthly, Rarely, Never
        if pd.isna(frequency_code):
            return 0
        return usage_factors[frequency_code - 1]

    # Extract relevant variables from the dataframe
    car_usage_days = df['C1_Car_Usage']
    car_type_code = df['C2_Car_type']
    travel_distance_code = df['C3_Travel_Distance']
    public_transport_frequency = df['C4_Public_Transport']
    public_transport_distance_code = df['Q74']
    flight_frequency = df['C5_Air_Travel']
    long_distance_train_frequency = df['C4_Public_Transport2']

    # Calculate weekly distances
    weekly_car_distance = np.vectorize(calculate_weekly_distance)(car_usage_days, travel_distance_code)
    weekly_public_transport_distance = np.vectorize(calculate_weekly_distance)(public_transport_frequency, public_transport_distance_code)

    # Map car type codes to emission factors
    car_emission_factors = np.vectorize(lambda code: emission_factors.get(map_car_type(code), 0))(car_type_code)
    public_transport_usage_factor = np.vectorize(map_public_transport_usage)(public_transport_frequency)
    train_usage_factor = np.vectorize(map_public_transport_usage)(long_distance_train_frequency)

    # Calculate emissions
    car_emissions = weekly_car_distance * car_emission_factors * 52
    public_transport_emissions = weekly_public_transport_distance * emission_factors["Public Transport"] * 52 * public_transport_usage_factor
    flight_emissions = np.where(pd.isna(flight_frequency), 0, flight_frequency * 500 * emission_factors["Flights"])  # Assuming 1000 km per flight
    long_distance_train_emissions = train_usage_factor * 100 * 365 * emission_factors["Long Distance Train"]  # Assuming 100 km per trip
    # Total transportation emissions
    total_transport_emissions = car_emissions + public_transport_emissions + flight_emissions + long_distance_train_emissions

    # Add the total transport emissions to the dataframe
    df['total_transport_emissions'] = total_transport_emissions

    # Print the first few rows of the dataframe with the calculated emissions
    print(df.head())
    return df

########### Calculation of the carbon footprint of food consumption #############
def calculate_food_emissions(df, emission_factors_food=None):
    # 碳排放系数
    if emission_factors_food is None:
        emission_factors_food = {
            "Meat-based meals": 3.07,  # kg CO2 per meal
            "Vegan meals": 0.25,  # kg CO2 per meal
            "Vegetarian meals": 0.68,  # kg CO2 per meal
            "Dairy Products": 327.1728 / 1000  # kg CO2 per liter, assuming 1 serving = 1 liter
        }

    # 从数据框中提取相关变量
    meat_meals_per_week = df['F3_Q28_1']
    vegan_meals_per_week = df['F3_Q28_2']
    vegetarian_meals_per_week = df['F3_Q28_3']
    dairy_products_per_week = df['F3_Q28_4']

    # 计算来自食物消费的年碳排放量
    meat_emissions = meat_meals_per_week * 52 * emission_factors_food["Meat-based meals"]
    vegan_emissions = vegan_meals_per_week * 52 * emission_factors_food["Vegan meals"]
    vegetarian_emissions = vegetarian_meals_per_week * 52 * emission_factors_food["Vegetarian meals"]
    dairy_emissions = dairy_products_per_week * 52 * emission_factors_food["Dairy Products"]

    # 计算总的食物碳排放量
    total_food_emissions = meat_emissions + vegan_emissions + vegetarian_emissions + dairy_emissions

    # 将总的食物碳排放量添加到数据框中
    df['total_food_emissions'] = total_food_emissions

    return df


########### Calculation of the carbon footprint of housing #############


def calculate_housing_emissions(data, zip_data=None, emission_factors_housing=None, electricity_prices=None):
    if emission_factors_housing is None:
        emission_factors_housing = {
            "WaterCFC": 26.5,  # kg CO2/year
            "Electricity": {
                "Average": 0.513,
                "Texas": 0.641855,
                "Western": 0.461226,
                "Eastern": 0.572386
            },
            "NaturalGas": 0.055  # kg CO2/thousand cubic feet
        }
    if zip_data is None:
        import requests
        url = "https://raw.githubusercontent.com/yebarryallen/SECFC/main/zip_data.csv"
        r = requests.get(url)
        #直接下载读取csv文件，不要保存
        zip_data = pd.read_csv(url)


    if electricity_prices is None:
        electricity_prices = {
            "state": ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA",
                      "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM",
                      "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA",
                      "WV", "WI", "WY"],
            "price": [12.41, 22.54, 13.16, 9.99, 19.90, 12.28, 21.62, 13.21, 12.05, 11.37, 12.26, 32.76, 10.58, 12.56,
                      12.02, 13.81, 11.56, 10.56, 9.37, 16.16, 13.92, 21.11, 16.07, 14.09, 11.55, 13.23, 11.85, 11.31,
                      11.67, 19.63, 15.64, 13.37, 19.30, 11.24, 12.07, 12.64, 10.72, 11.02, 14.38, 18.64, 12.91, 12.39,
                      10.79, 11.36, 10.63, 18.50, 12.40, 9.79, 11.57, 14.28, 12.30]
        }
        electricity_prices_df = pd.DataFrame(electricity_prices)

    def classify_state(zip_code, zip_data):
        matched_state = zip_data[(zip_code >= zip_data['Zip Min']) & (zip_code <= zip_data['Zip Max'])]['ST'].unique()
        if len(matched_state) == 1:
            return matched_state[0]
        else:
            return np.nan

    def classify_zip_code(zip_code, zip_data):
        state = classify_state(zip_code, zip_data)
        west_states = ["WA", "OR", "CA", "ID", "NV", "UT", "AZ", "MT", "WY", "CO", "NM", "HI", "AK"]
        east_states = ["ME", "NH", "MA", "RI", "CT", "NY", "NJ", "DE", "MD", "VA", "NC", "SC", "GA", "FL", "VT", "PA",
                       "WV", "OH", "MI"]
        if not pd.isna(state):
            if state in west_states:
                return "West"
            elif state in east_states:
                return "East"
            elif state == "TX":
                return "Texas"
            else:
                return "Other"
        else:
            return "Zip code not found in dataset"

    data['US_Zip_Code'] = pd.to_numeric(data['US_Zip_Code'], errors='coerce')
    data['state'] = data['US_Zip_Code'].apply(lambda x: classify_state(x, zip_data))
    data['region'] = data['US_Zip_Code'].apply(lambda x: classify_zip_code(x, zip_data))
    data['electricity_emission_factor'] = data['region'].apply(
        lambda x: emission_factors_housing['Electricity'][x] if x in emission_factors_housing['Electricity'] else
        emission_factors_housing['Electricity']['Average'])
    data['electricity_price'] = data['state'].apply(
        lambda x: electricity_prices_df[electricity_prices_df['state'] == x]['price'].values[0] if x in
                                                                                                   electricity_prices_df[
                                                                                                       'state'].values else np.nan)

    data['monthly_electricity_kWh'] = (data['E2_Electricity_bill_1'] * 100) / data['electricity_price']
    data['monthly_gas_cubic_feet'] = data['E3_natural_gas_bill_1'] / 10
    data['annual_electricity_emissions'] = data['monthly_electricity_kWh'] * 12 * data['electricity_emission_factor']
    data['annual_gas_emissions'] = data['monthly_gas_cubic_feet'] * 12 * emission_factors_housing['NaturalGas']
    data['annual_water_emissions'] = emission_factors_housing['WaterCFC']
    data['Family_size'] = data[['Family_size_6', 'Family_size_14', 'Family_size_15']].sum(axis=1).astype(int)
    data['total_housing_emissions'] = (data['annual_electricity_emissions'] + data['annual_gas_emissions'] + data[
        'annual_water_emissions'])/(data['Family_size'])
    return data







######### Calculation of the carbon footprint of living consumption ############


# 计算函数
def calculate_consumption_emissions(df, emission_factors=None):
    if emission_factors is None:
        emission_factors = {
            "FoodDelivery": 0.349757961,  # kg CO2/USD
            "DiningOut": 0.010974672,  # kg CO2/USD
            "HotelStays": 0.016436699,  # kg CO2/USD
            "TobaccoProducts": 0.009542055,  # kg CO2/USD
            "AlcoholDrinks": 0.042726645,  # kg CO2/USD
            "Entertainment": 0.009474576,  # kg CO2/USD
            "Healthcare": 0.014611029,  # kg CO2/USD
            "Clothing": 0.018380588  # kg CO2/USD
        }
    df["FoodDeliveryEmission"] = df["Q84_1"] * emission_factors["FoodDelivery"]
    df["DiningOutEmission"] = df["Q84_2"] * emission_factors["DiningOut"]
    df["HotelStaysEmission"] = df["Q84_4"] * emission_factors["HotelStays"]
    df["TobaccoProductsEmission"] = df["Q84_5"] * emission_factors["TobaccoProducts"]
    df["AlcoholDrinksEmission"] = df["Q84_6"] * emission_factors["AlcoholDrinks"]
    df["EntertainmentEmission"] = df["Q84_7"] * emission_factors["Entertainment"]
    df["HealthcareEmission"] = df["Q84_8"] * emission_factors["Healthcare"]

    # 计算每年服装购买的排放量
    annual_clothing_spending = df["CL1_Q31"].apply(lambda x: [600, 420, 300, 120, 60][x - 1])  # 假设每年服装花费
    df["ClothingEmission"] = annual_clothing_spending * emission_factors["Clothing"]

    # 计算总排放量
    df["ConsumptionEmissions"] = df[[
        "FoodDeliveryEmission", "DiningOutEmission", "HotelStaysEmission",
        "TobaccoProductsEmission", "AlcoholDrinksEmission", "EntertainmentEmission",
        "HealthcareEmission", "ClothingEmission"
    ]].sum(axis=1)

    return df


#####################计算总的碳排放量####################

def calculate_all_emissions(df, plot=False):
    # Calculate total emissions
    df["TotalEmissions"] = df[[
        "total_transport_emissions", "total_food_emissions",
        "total_housing_emissions", "ConsumptionEmissions"
    ]].sum(axis=1)
    if plot:
        import matplotlib.pyplot as plt
        #绘图时候删去drop缺失值 和 inf 值
        df['TotalEmissions'] = df['TotalEmissions'].replace([np.inf, -np.inf], np.nan).dropna()
        plt.hist(df['TotalEmissions'], bins=20)
        plt.title("Distribution of Total Emissions (kg CO2))")
        plt.show()
    return df

