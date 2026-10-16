import pandas as pd
import numpy as np
s=pd.Series([1,3,6,np.nan,44,1])#np.nan=Not a Number,代表缺失值，只要Series里面存在nan,整个序列的数据类型就会变成float64,int存不了NaN
print(s)
print('==========================')
dates=pd.date_range('20160101',periods=6)#freq='D'按天生成 连续日期索引
print(dates)
print('=============')
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['A','B','C','D'])
#二维表格         随机生成                  行索引           列名
print(df)
print('=======================')
df1=pd.DataFrame(np.arange(12).reshape((3,4)))#没有指定 index 和 columns，自动生成默认 0,1,2 行索引；0,1,2,3 列索引
print(df1)
print('===========================')
df2=pd.DataFrame({'A':1.,
                  'B':pd.Timestamp('20160101'),
                  'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                  'D':np.array([3]*4,dtype='int32'),
                  'E':pd.Categorical(['test','train','test','train']),
                  'F':'foo'
                  })
print(df2)
print('===========================')
print(df2.dtypes)
print('===========================')
print(df2.index)#查看**行索引**：`RangeIndex(start=0, stop=4, step=1)` 也就是 0,1,2,3
print('===========================')
print(df2.columns)#查看**所有列名**：`Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')`
print('===========================')
print(df2.values)#取出表格**纯数值数组（去掉行列标签）**，变成 numpy array。
print('===========================')
print(df2.describe())#**描述性统计**，只对数值型列 (A,C,D) 自动计算：
#count (数量)、mean (均值)、std (标准差)、min、25% 分位数、50%、75%、max
#时间、字符串、分类列不会出现在 describe 结果里。
print('===========================')
print(df2.T)#**矩阵转置**：行变列，列变行。原来的列 A/B/C/D/E/F 变成行索引；原来 0,1,2,3 行变成列
print('===========================')
print(df2.sort_index(axis=1,ascending=False))#- `axis=1`：对**列**操作（axis=0 是行）

#`ascending=False`：降序
print('===========================')
print(df2.sort_values(by='E'))#按**某一列的值排序**
#`by='E'`：根据 E 列的值排序
#E 列的值是`test、train、test、train`，排序后：所有 test 放前面，train 放后面。