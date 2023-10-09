# try to build the best Gen after 100 priod Time
import numpy as np
import pandas as pd
from random import *
# import bs4 as bs

""""
صبوری = patience
running away from work = فرار از کار
hardworker = سختکوش، پرتلاش
age = سن
height = بلندی قامت
Well-dressed = خوش پوشی
Lying = دروغگویی
Society = جامعه
"""

# def First_Society():
first_Society = []
for i in range(1, 101):
    crom = {"hard-worker": np.random.randint(-10, 11),
                "age": np.random.randint(-10, 11),
                "running_away_from_work": np.random.randint(-10, 11),
                "patience": np.random.randint(-10, 11),
                "height": np.random.randint(-10, 11),
                "Well-dressed": np.random.randint(-10, 11),
                "Lying": np.random.randint(-10, 11)}
    Fittness_Func = (crom["hard-worker"] * 5) + (crom["age"]) - (crom["running_away_from_work"]) + \
                    (crom["patience"]*2) + (crom["height"]) + (crom["Well-dressed"] * 2) - (crom["Lying"] * 3)
    crom["Fittness_Func"] = Fittness_Func
    first_Society.append(crom)

data = pd.DataFrame(first_Society, index=range(1, 101)).to_string()
    # return data
print(data)

# print(First_Society())


ten_percent_of_Society = []
for _ in range(10):
    selected = randint(1,101)
    new_so = first_Society[selected-1]
    ten_percent_of_Society.append(new_so)
    print(selected)
print()
new_mutatoin_data = pd.DataFrame(ten_percent_of_Society, index=range(101, 111))
print(new_mutatoin_data.to_string())




random_gen_selectoin = randint(0, 6)
new_gen_value = np.random.randint(-10, 11)
print("random_select_gen :", random_gen_selectoin)
print("new_value_gen = ", new_gen_value)
new_mutatoin_data.iloc[:,random_gen_selectoin] = new_gen_value
print(new_mutatoin_data.to_string())


for i in range(len(new_mutatoin_data)):
    Fittness_Func = ((new_mutatoin_data.iloc[i,0]) * 5) + (new_mutatoin_data.iloc[i,1]) - (new_mutatoin_data.iloc[i,2]) +\
                    (new_mutatoin_data.iloc[i,3]*2) + (new_mutatoin_data.iloc[i,4]) + (new_mutatoin_data.iloc[i,5] * 2) -\
                    (new_mutatoin_data.iloc[i,6] * 3)
    new_mutatoin_data.loc[i,"Fittness_Func"] = Fittness_Func
print(new_mutatoin_data.to_string())






def Generatoin():
    def mutatoin():
        pass

    def cross_over():
        pass

    pass
