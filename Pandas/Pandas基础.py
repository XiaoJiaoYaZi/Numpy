import pandas as pd
import numpy as np

#设置最大行，最大列
pd.set_option('max_columns',8,'max_rows',10)

movies = pd.read_csv('../data/movie.csv')
#head默认查看前5行数据,head(n)查看前n行
print(movies.head())

#提取列索引
columns = movies.columns
#提取行索引
index = movies.index
#提取数据
data = movies.values

#访问index
value = index.values
#index 是个列表，可以索引，切片等操作
print(value[1])

#访问columns
value = columns.values
print(value[0])

#查看各个列的类型
print(movies.dtypes)

#显示各个类型的数量
movies.get_dtype_counts()

#选取一列，座位Series
index0 = movies['color']
index0 = movies.color
print(type(index0))

#查看列名
inde_name = index0.name

#单列Series转化为DataFrame
head = index0.to_frame().head()

#选取director和actor_1_fb_likes两列
director = movies.director_name
actor_1_fb_likes = movies['actor_1_facebook_likes']
head1 = director.head()
head2 = actor_1_fb_likes.head()
#统计数量
count1 = director.value_counts()
count2 = actor_1_fb_likes.value_counts()

print(director.size,director.shape,len(director))

#查看director有多少非空值
count_empty = director.size - director.count()


#中位分位数
quantitle = actor_1_fb_likes.quantile(.5)
print('quantitle:.5:',quantitle)

#最小值，最大值，品均值，中位数，标准差，总和
print('min:',actor_1_fb_likes.min(),
      'max:',actor_1_fb_likes.max(),
      'mean:',actor_1_fb_likes.mean(),
      'median:',actor_1_fb_likes.median(),
      'std:',actor_1_fb_likes.std(),
      'sum:',actor_1_fb_likes.sum())

print(actor_1_fb_likes.describe())
print(director.describe())

#各个十分之一的分位数
print(actor_1_fb_likes.quantile([.1,.2,.3,.4,.5,.6,.7,.8,.9]))










