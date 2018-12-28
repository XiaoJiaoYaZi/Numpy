import pandas as pd
import numpy as np


#读取college的数据集，查看city的前5行
college = pd.read_csv('../data/college.csv',index_col='INSTNM')
city = college['CITY']
city_head = city.head()

#iloc可以公国整数选取
iloc_3 = city.iloc[3]
#iloc通过整数列表选取多行，返回结果是Series
ilocs = city.iloc[[1,2,3]]
#选取等分的数据，可以用切片语法
iloc_1 = city.iloc[1:10:2]

#loc只能接受行索引标签
loc = city.loc['Heritage Christian University']

#随机选择4个标签
np.random.seed(1)
labels = list(np.random.choice(city.index,4))

#通过标签选择多行
locs = city.loc[labels]

#也可以使用切片语法选择多个
loc_q = city.loc['Alabama State University':'Reid State Technical College':10]

#也可以不适用loc，直接使用python语法
loc_q_p = city['Alabama State University':'Reid State Technical College':10]

#如果只选取一项，并保留其Series的类型，则传入一个只包含一项的列表
loc_1 = city.iloc[[3]]

#使用loc切片要注意，如果start索引在stop索引之后，会返回空，并且不会报警
loc_e = city.loc['Reid State Technical College':'Alabama State University':10]

# .index.tolist()可以直接提取索引标签，生成一个列表
ilist = city.iloc[[60,99,3]].index.tolist()

#选取前3行和前4列
i3_4 = college.iloc[:3,:4]

#选取所有行的2列
ia_2 = college.iloc[:,[4,6]].head()

#选取不连续的行和列
ii_i = college.iloc[[100,200],[7,15]]

#iloc选取一个标量值
i = college.iloc[5,-4]

#loc选取一个标量值
ii = college.loc['The University of Alabama', 'PCTFLOAN']

#iloc对列切片，并只选取一列
i_q = college.iloc[90:80:-2,5]

#loc对行切片，并只选取一列
start = 'Empire Beauty School-Flagstaff'
stop = 'Arizona State University-Tempe'
ii_q = college.loc[start:stop:-2, 'RELAFFIL']

# 用索引方法get_loc，找到指定列的整数位置
col_start = college.columns.get_loc('UGDS_WHITE')
col_end = college.columns.get_loc('UGDS_UNKN') + 1
#col_start, col_end
iii = college.iloc[:5,col_start:col_end]

## index()方法可以获得整数行对应的标签名
row_start = college.index[10]
row_end = college.index[15]
iii_row = college.loc[row_start:row_end, 'UGDS_WHITE':'UGDS_UNKN']

# 通过将行标签赋值给一个变量，用loc选取
loc_1_1 = college.loc['Texas A & M University-College Station','UGDS_WHITE']
# at可以实现同样的功能
loc_1_1_at = college.loc['Texas A & M University-College Station','UGDS_WHITE']

#.iat和.at只接收标量值，是专门用来取代.iloc和.loc选取标量的，可以节省大概2.5微秒。
at = college.at['Texas A & M University-College Station','UGDS_WHITE']

# Series对象也可以使用.iat和.at选取标量
state = college['STABBR']
at_s_i = state.iat[1000]
at_s = state.at['Stanford University']

college = college.sort_index()
loc_sp_su = college.loc['Sp':'Su']

# 可以用is_monotonic_increasing或is_monotonic_decreasing检测字母排序的顺序
print(college.index.is_monotonic_decreasing)
# 字母逆序选取
college = college.sort_index(ascending=False)
loc_E_B = college.loc['E':'B']












