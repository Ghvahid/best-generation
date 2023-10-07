# try to build the best Gen after 100 priod Time
import numpy as np
import pandas as pd


""""
صبوری = patience
running away from work = فرار از کار
hardworker = سختکوش، پرتلاش
age = سن
height = بلندی قامت
Well-dressed = خوش پوشی
Lying = دروغگویی
"""

crom_dic = {"hardworker": np.random.randint(-10,11),
            "age": np.random.randint(-10,11),
            "running away from work": np.random.randint(-10,11),
            "patience": np.random.randint(-10,11),
            "height": np.random.randint(-10,11),
            "Well-dressed": np.random.randint(-10,11),
            "Lying": np.random.randint(-10,11)}
print(crom_dic)

Fittness_Func = (crom_dic["hardworker"]**3) + (crom_dic["age"]) + (crom_dic["Lying"]*2) + (crom_dic["running away from work"]) \
                + (crom_dic["patience"]) + (crom_dic["height"]) + (crom_dic["Well-dressed"]*2)
print(Fittness_Func)
generatoin = []
for _ in range(100):
    crom_dic = {"hardworker": np.random.randint(-10, 11),
                "age": np.random.randint(-10, 11),
                "running away from work": np.random.randint(-10, 11),
                "patience": np.random.randint(-10, 11),
                "height": np.random.randint(-10, 11),
                "Well-dressed": np.random.randint(-10, 11),
                "Lying": np.random.randint(-10, 11)}
    Fittness_Func = (crom_dic["hardworker"] ** 3) + (crom_dic["age"]) + (crom_dic["Lying"] * 2) + (crom_dic["running away from work"]) + (crom_dic["patience"]) + (crom_dic["height"]) + (crom_dic["Well-dressed"] * 2)
    generatoin.append(Fittness_Func)
    print(crom_dic)
    print(Fittness_Func)

print(sorted(generatoin))