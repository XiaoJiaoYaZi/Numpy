import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

movie = pd.read_csv('../data/movie.csv',index_col='movie_title')

# 判断电影时长是否超过两小时
movie_2_hours = movie['duration'] > 120

# 有多少时长超过两小时的电影
sum_2_hours = movie_2_hours.sum()

# 超过两小时的电影的比例
mean_2_hours = movie_2_hours.mean()

# 用describe()输出一些该布尔Series信息
descrip_2_hours = movie_2_hours.describe()

# 实际上，dureation这列是有缺失值的，要想获得真正的超过两小时的电影的比例，需要先删掉缺失值
movie_2_hours2 = movie['duration'].dropna().gt(120)

# 统计False和True值的比例
counts = movie_2_hours2.value_counts(normalize=True)

# 比较同一个DataFrame中的两列
actors = movie[['actor_1_facebook_likes','actor_2_facebook_likes']]
means_actor = (actors['actor_1_facebook_likes'] > actors['actor_2_facebook_likes']).mean()

# 创建多个布尔条件
criterial1 = movie['imdb_score'] >8
criterial2 = movie['content_rating'] == 'PG-13'
criterial3 = (movie['title_year'] <2000) | (movie['title_year']>2010)

# 在Pandas中，位运算符（&, |, ~）的优先级高于比较运算符，因此如过前面的条件3不加括号，就会报错

final_crit_a = criterial1 & criterial2 & criterial3
# 用最终的布尔条件过滤数据
final = movie[final_crit_a]

# 使用loc，对指定的列做过滤操作，可以清楚地看到过滤是否起作用
cols = ['imdb_score', 'content_rating', 'title_year']
movie_filtered = movie.loc[final_crit_a, cols]


#用标签索引代替布尔索引
college = pd.read_csv('../data/college.csv')
TX = college[college['STABBR'] == 'TX'].head()
college2 = college.set_index('STABBR')
TX2 = college2.loc['TX'].head()

# 使用布尔索引和标签选取多列
states =['TX', 'CA', 'NY']
TX3 = college2.loc[states].head()


#用唯一和有序索引选取
# 将college2排序，存储成另一个对象，查看其是否有序
college3 = college2.sort_index()
print(college3.index.is_monotonic)

# 使用INSTNM作为行索引，检测行索引是否唯一
college_unique = college.set_index('INSTNM')
print(college_unique.index.is_unique)

# 用布尔索引选取斯坦福大学
stanford = college[college['INSTNM'] == 'Stanford University']

# 使用CITY和STABBR两列作为行索引，并进行排序
college.index = college['CITY'] + ',' + college['STABBR']
college = college.sort_index()

# 选取所有Miami, FL的大学
Miami_FL = college.loc['Miami,FL'].head()


# 读取Schlumberger stock数据集，行索引设为Date列，并将其转变为DatetimeIndex
slb = pd.read_csv('../data/slb_stock.csv', index_col='Date', parse_dates=['Date'])

# 选取Close这列，用describe返回统计信息
slb_close = slb['Close']
slb_summary = slb_close.describe(percentiles=[.1, .9])

upper_10 = slb_summary.loc['90%']
lower_10 = slb_summary.loc['10%']
criteria = (slb_close < lower_10) | (slb_close > upper_10)
slb_top_bottom_10 = slb_close[criteria]

# 过滤出的数据使用灰色，所有的收盘价使用黑色，用matplotlib在十分之一和十分之九分位数位置画横线

slb_close.plot(color='black', figsize=(12,6))
slb_top_bottom_10.plot(marker='o', style=' ', ms=4, color='yellow')
xmin = criteria.index[0]
xmax = criteria.index[-1]
plt.hlines(y=[lower_10, upper_10], xmin=xmin, xmax=xmax,color='black')
plt.show()







































