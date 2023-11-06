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
data = pd.DataFrame(first_Society, index=range(1, 101))
print(data)

#Create 10 new people from first society ----->> def mutation
random_gen_selectoin = randint(0, 6)
new_gen_value = np.random.randint(-10, 11)
print("random_select_gen :", random_gen_selectoin)
print("new_value_gen = ", new_gen_value)

ten_percent_of_Society = []
for _ in range(10):
    selected = randint(1,100)
    # print(selected)
    new_so =first_Society[selected-1]
    # print(list(new_so.keys()))
    l_keys = list(new_so.keys())
    x = l_keys[random_gen_selectoin]
    # print(x)
    new_so[f"{x}"] = new_gen_value
    Fittness_Func = (new_so["hard-worker"] * 5) + (new_so["age"]) - (new_so["running_away_from_work"]) + \
                    (new_so["patience"] * 2) + (new_so["height"]) + (new_so["Well-dressed"] * 2) - (new_so["Lying"] * 3)
    new_so["Fittness_Func"] = Fittness_Func
    ten_percent_of_Society.append(new_so)
# print(ten_percent_of_Society)
print("-"*40)
new_mutatoin_data = pd.DataFrame(ten_percent_of_Society, index=range(101, 111))
print(new_mutatoin_data)
# end of def mutation


# Create def Crossover
random_gen_selectoin = randint(0, 6)
print("random_select_gen :", random_gen_selectoin)
secend_ten_percent_of_Society = []
for _ in range(5):
    selected_one = randint(1,100)
    selected_two = randint(1,100)
    # print(selected_one)
    # print(selected_two)
    new_so_1 =first_Society[selected_one-1]
    new_so_2 =first_Society[selected_two-1]
    # print(new_so_1)
    # print(new_so_2)
    new_1 = dict(list(new_so_1.items())[:random_gen_selectoin] + list(new_so_2.items())[random_gen_selectoin:])
    new_2 = dict(list(new_so_2.items())[:random_gen_selectoin] + list(new_so_1.items())[random_gen_selectoin:])
    # print(new_1)
    # print(new_2)
    Fittness_Func = (new_1["hard-worker"] * 5) + (new_1["age"]) - (new_1["running_away_from_work"]) + \
                    (new_1["patience"] * 2) + (new_1["height"]) + (new_1["Well-dressed"] * 2) - (new_1["Lying"] * 3)
    new_1["Fittness_Func"] = Fittness_Func
    secend_ten_percent_of_Society.append(new_1)

    Fittness_Func = (new_2["hard-worker"] * 5) + (new_2["age"]) - (new_2["running_away_from_work"]) + \
                    (new_2["patience"] * 2) + (new_2["height"]) + (new_2["Well-dressed"] * 2) - (new_2["Lying"] * 3)
    new_2["Fittness_Func"] = Fittness_Func
    secend_ten_percent_of_Society.append(new_2)
# print(secend_ten_percent_of_Society)
print("+-"*40)
new_crossover_data = pd.DataFrame(secend_ten_percent_of_Society, index=range(111, 121))
print(new_crossover_data)
# End of Create Crossover def

#tajmih 3 dataframe dar yek jadval 120 adadi
x = [data, new_mutatoin_data, new_crossover_data]
all_society = pd.concat(x)
# print(all_society.to_string())

all_society.sort_values("Fittness_Func", ascending=True,inplace=True , ignore_index=True )
# m = min(all_society["Fittness_Func"])
# print(m)
# print(all_society)
'''Delete first 20 lowest Fittness from society and hold other 100 human'''
for i in range(20):
    all_society = all_society.drop(index=[i])


print(all_society)

