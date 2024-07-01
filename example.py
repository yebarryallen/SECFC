import SECFC
import pandas as pd

# example usage
data= pd.read_csv("standard data.csv")


test_df = SECFC.calculate_personal_emissions(data)
test_df = SECFC.calculate_food_emissions(test_df)
test_df = SECFC.calculate_housing_emissions(test_df)
test_df = SECFC.calculate_consumption_emissions(test_df)
test_df= SECFC.calculate_all_emissions(test_df, plot=True)



