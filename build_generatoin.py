# try to build the best Gen after 100 priod Time
import numpy as np
import pandas as pd


rank = np.arange(-10, 11)
print(rank)

rank_rd = np.random.randint(-10,11)
print(rank_rd)
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