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

sum_nan = (college_ugds_ == np.nan).sum()

ugd_count = college_ugds_.count(axis=0)

# 使用累积求和cumsum()可以很容易看到白人、黑人、西班牙裔的比例
college_ugds_cumsum = college_ugds_.cumsum(axis=1)

# UGDS_HISP一列降序/升序排列
college_ugds_cumsum_sort=college_ugds_cumsum.sort_values("UGDS_BLACK",ascending=True)

###########


# 如果所有列都是缺失值，则将其去除
college_ugds_ = college_ugds_.dropna(how='all')


# 用大于或等于方法ge()，将DataFrame变为布尔值矩阵
diversity_metric = college_ugds_.ge(.15).sum(axis='columns')

# 使用value_counts()，查看分布情况
diversity_metric.value_counts()

## 查看哪些学校种群比例超过15%的数量多
diversity_metric.sort_values(ascending = False).head()

# 用loc()方法查看对应行索引的行











