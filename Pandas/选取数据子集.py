import pandas as pd
import numpy as np

college = pd.read_csv('../data/college.csv')
T = None
with pd.option_context('display.max_rows',8):
    T = college.describe(include=[np.number]).T
    T = college.describe(include=[np.object,pd.Categorical]).T

# 列出每列的数据类型，非缺失值的数量，以及内存的使用
info = college.info()

# 选取五列
different_cols = ['RELAFFIL', 'SATMTMID', 'CURROPER', 'INSTNM', 'STABBR']
col2 = college.loc[:, different_cols]

# 用memory_usage方法查看每列的内存消耗
original_mem = col2.memory_usage(deep=True)




















