
import pandas as pd

from SECFC import diets_calc
from SECFC import trans_calc
from SECFC import consump_calc
from SECFC import housing_calc
from SECFC import total_emis_calc
# example usage
data = {
    'C1_Car_Usage': [5, 3, 0, 7, 2],  # 每周使用汽车的天数
    'C2_Car_type': [1, 2, 2, 3, 4],  # 汽车类型编码
    'C3_Travel_Distance': [2, 1, 4, 3, 2],  # 出行距离编码
    'C4_Public_Transport': [3, 2, 1, 4, 0],  # 公共交通频率编码
    'C5_Public_Transport_distance': [1, 2, 3, 4, 1],  # 公共交通距离编码
    'C5_Air_Travel': [2, 1, 1, 3, 0],  # 飞行频率
    'C4_Public_Transport2': [3, 2, 1, 0, 4],  # 长途火车频率编码
    'F3_Q28_1': [7, 5, 6, 2, 3],  # 每周肉类餐数量
    'F3_Q28_2': [3, 4, 2, 1, 5],  # 每周素食餐数量
    'F3_Q28_3': [1, 2, 3, 4, 2],  # 每周植物性餐数量
    'F3_Q28_4': [4, 2, 5, 3, 1],  # 每周乳制品数量
    'US_Zip_Code': [90210, 10001, 73301, 60616, 33101],  # 邮政编码
    'E2_Electricity_bill_1': [100, 150, 200, 250, 300],  # 月电费
    'E3_natural_gas_bill_1': [50, 75, 100, 125, 150],  # 月燃气费
    'Family_size_6': [1, 2, 3, 4, 5],  # 家庭成员数1
    'Family_size_14': [0, 1, 0, 1, 0],  # 家庭成员数2
    'Family_size_15': [0, 0, 1, 0, 1],  # 家庭成员数3
    'GOODS_1': [200, 300, 400, 500, 600],  # 外卖花费
    'GOODS_2': [100, 200, 300, 400, 500],  # 外出就餐花费
    'GOODS_4': [150, 250, 350, 450, 550],  # 酒店住宿花费
    'GOODS_5': [50, 100, 150, 200, 250],  # 烟草产品花费
    'GOODS_6': [75, 125, 175, 225, 275],  # 酒精饮品花费
    'GOODS_7': [60, 110, 160, 210, 260],  # 娱乐花费
    'GOODS_8': [80, 130, 180, 230, 280],  # 医疗保健花费
    'PETS_1': [1, 0, 1, 0, 1],  # 狗数量
    'PETS_2': [0, 1, 0, 1, 0],  # 猫数量
    'CL1_Q31': [1, 2, 3, 4, 5]  # 年服装花费级别
}

data = pd.DataFrame(data)
# data = pd.read_csv('standard data.csv')



test_df = diets_calc(data)
test_df = trans_calc(test_df)
test_df = consump_calc(test_df)
test_df = housing_calc(test_df)
test_df= total_emis_calc(test_df, plot=True)



