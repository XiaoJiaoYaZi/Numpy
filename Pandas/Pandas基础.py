import pandas as pd
import numpy as np

#设置最大行，最大列
pd.set_option('max_columns',8,'max_rows',10)

movies = pd.read_csv('../data/movie.csv')
#head默认查看前5行数据,head(n)查看前n行
print(movies.head())
pd
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
director = movies['director_name']
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
quantile = actor_1_fb_likes.quantile([.1,.2,.3,.4,.5,.6,.7,.8,.9])
#非空值
isnull = director.isnull()
#填充缺失值
actor_1_fb_likes_filled = actor_1_fb_likes.fillna(0)
#删除缺失值
actor_1_fb_likes_drop = actor_1_fb_likes.dropna()


#value_counts()可以返回频率
value_counts = director.value_counts(normalize=True)

#判断是否有缺失值
print('hasnans:',director.hasnans)

#判断是否是非缺失值
notnull = director.notnull()

############计算相关###########

#选取imdb_score列，并+1
imdb_socre = movies['imdb_score']
imdb_socre1 = imdb_socre+1#imdb_score.add(1)
#每列*2.5
imdb_socre2 = imdb_socre*2.5#imdb_score.mul(2.5)
#每列除以7的余数
imdb_socre3 = imdb_socre/7#imdb_score.floordiv(7
#判断是否 >7
imdb_socre4 = imdb_socre >7#imdb_score.gt(7)
#判断等于
imdb_socre5 = imdb_socre.equals(5)
#取模
imdb_socre6 = imdb_socre.astype(int).mod(5)

#计数，查看前3
head3 = director.value_counts().head()

#统计缺失值的数量
sum_isnull = actor_1_fb_likes.isnull().sum()

#缺失值填充为0、转换为整型、查看前五
head4 = actor_1_fb_likes.fillna(0).astype(int).head()

#缺失值的比例
mean_isnull = actor_1_fb_likes.isnull().mean()

#set_index() 给行索引命名
movies2 = movies.set_index('movie_title')
#复原索引
movies2.reset_index()

#通过rename（）重命名
movies = pd.read_csv('../data/movie.csv',index_col='movie_title')
idx_rename = {'Avatar':'Retava','Spectre':'Ertceps'}
col_rename = {'director_name':'Direct Name','num_critic_for_reviews':'Critical Reviews'}
head_rename = movies.rename(index=idx_rename,columns=col_rename).head()

index_list = movies.index.tolist()
column_list = movies.columns.tolist()

#添加和删除列
movies['has_seen'] = 0

movies['actor_director_facebook_likes'] = (movies['actor_1_facebook_likes'] +
                                           movies['actor_2_facebook_likes'] +
                                           movies['actor_3_facebook_likes'] +
                                           movies['director_facebook_likes'])
#insert 原地插入列
profix_index = movies.columns.get_loc('gross')+1
movies.insert(loc= profix_index,column='profix',value=movies['gross']-movies['budget'])
movies.drop(columns = ['has_seen',],axis=1)
#has_seen = movies['has_seen'].head()
movies = movies.T
movies.to_csv('movie.csv')



