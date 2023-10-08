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

# Fitt_count = []
Nasl = []
for i in range(1,101):
    crom_dic = {"hard-worker": np.random.randint(-10, 11),
                "age": np.random.randint(-10, 11),
                "running_away_from_work": np.random.randint(-10, 11),
                "patience": np.random.randint(-10, 11),
                "height": np.random.randint(-10, 11),
                "Well-dressed": np.random.randint(-10, 11),
                "Lying": np.random.randint(-10, 11)}

    Fittness_Func = (crom_dic["hard-worker"] ** 3) + (crom_dic["age"]) + (crom_dic["Lying"] * 2) + (crom_dic["running_away_from_work"]) + (crom_dic["patience"]) + (crom_dic["height"]) + (crom_dic["Well-dressed"] * 2)
    crom_dic["Fittness_Func"] = Fittness_Func
    Nasl.append(crom_dic)
    # Fitt_count.append(Fittness_Func)

# print(Nasl)
# print(Fitt_count)
data = pd.DataFrame(Nasl, index=range(1, 101)).to_string()
print(data)

