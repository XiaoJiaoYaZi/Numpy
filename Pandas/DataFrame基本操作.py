import pandas as pd
import numpy as np

#选取多个DataFrame
movie = pd.read_csv('../data/movie.csv')
movie_actor_director = movie[['actor_1_name',
                              'actor_2_name',
                              'actor_3_name',
                              'director_name']]

#选取所有的 数 列值 include 为列的类型,string--object,numbers--number
number_all = movie.select_dtypes(include=['number'])
int_all = movie.select_dtypes(include=['int'])
dtypes = movie.dtypes

#filter()函数过滤选取多列
filter_like_all = movie.filter(like='facebook')
filter_item_all = movie.filter(items=['actor_1_name', 'asdf'])

#将列索引按照指定的顺序排序
columns = sorted(movie.columns,key=lambda k:len(k))
sorted_movie = movie[columns]

#每个列的值的个数
count = movie.count()
#每列的最小值
min_count = movie.min()

#分位数
percentiles = movie.describe(percentiles=[.1,.3,.99])

#空值的个数
num_null = movie.isnull().sum()

#设定skipna=False，没有缺失值的数值列才会计算结果
#skip_na = movie.min(skipna=False)

#**************运算符***************
college = pd.read_csv('../data/college.csv')
college_ugds_ = college.filter(like='UGDS_')
result = college_ugds_ == 'asdf'





















