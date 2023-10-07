# try to build the best Gen after 100 priod Time
import numpy as np
import pandas as pd
# import bs4 as bs

""""
صبوری = patience
running away from work = فرار از کار
hardworker = سختکوش، پرتلاش
age = سن
height = بلندی قامت
Well-dressed = خوش پوشی
Lying = دروغگویی
"""
# crom_dic = {"hardworker": np.random.randint(-10,11),
#             "age": np.random.randint(-10,11),
#             "running away from work": np.random.randint(-10,11),
#             "patience": np.random.randint(-10,11),
#             "height": np.random.randint(-10,11),
#             "Well-dressed": np.random.randint(-10,11),
#             "Lying": np.random.randint(-10,11)}
# Fittness_Func = (crom_dic["hardworker"]**3) + (crom_dic["age"]) + (crom_dic["Lying"]*2) + (crom_dic["running away from work"]) + (crom_dic["patience"]) + (crom_dic["height"]) + (crom_dic["Well-dressed"]*2)

generatoin = []
Nasl = []
for i in range(100):
    crom_dic = {"hardworker": np.random.randint(-10, 11),
                "age": np.random.randint(-10, 11),
                "running away from work": np.random.randint(-10, 11),
                "patience": np.random.randint(-10, 11),
                "height": np.random.randint(-10, 11),
                "Well-dressed": np.random.randint(-10, 11),
                "Lying": np.random.randint(-10, 11)}
    Fittness_Func = (crom_dic["hardworker"] ** 3) + (crom_dic["age"]) + (crom_dic["Lying"] * 2) + (crom_dic["running away from work"])\
                    + (crom_dic["patience"]) + (crom_dic["height"]) + (crom_dic["Well-dressed"] * 2)

    Nasl.append(crom_dic)
    generatoin.append({f"g{i+1}": Fittness_Func})

print(Nasl)
print(generatoin)
# print(sorted(generatoin))