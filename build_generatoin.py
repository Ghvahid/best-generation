# try to build the best Gen after 100 priod Time
import numpy as np
import pandas as pd
from random import randint
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
    Fittness_Func = (crom["hard-worker"] * 5) + (crom["age"]) - (crom["Lying"] * 3) - (crom["running_away_from_work"]) + (crom["patience"]*2) + (crom["height"]) + (crom["Well-dressed"] * 2)
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
new_mutatoin_data = pd.DataFrame(ten_percent_of_Society, index=range(101, 111)).to_string()
print(new_mutatoin_data)





def Generatoin():
    def mutatoin():
        pass

    def cross_over():
        pass

    pass
