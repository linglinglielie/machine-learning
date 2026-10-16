import pandas as pd
import numpy as np
dates=pd.date_range('20180101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(df)
print('===========================')
print(df['A'],df.A)
print('===========================')
print(df[0:3],df['20180102':'20180104'])
print('===========================')
print(df.loc['20180102'])#以标签来选择
print('===========================')
print(df.loc[:,['A','B']])
print('===========================')
print(df.loc['20180102',['A','B']])
print('==========select by position:iloc=================')
print(df.iloc[3,1])
print('===========================')
print(df.iloc[3:5,1:3])
print('==========================')
print(df.iloc[[1,3,5],1:3])
print('=========mixed selection:ix================')
#print(df.ix[:3,['A','B','C']])
#.ix**在 pandas 0.20 版本之后已经被废弃，不再推荐使用，运行会报警告**。
#ix 是混合索引，既可以按标签也可以按位置；现在官方推荐分开用 `loc`（标签）和 `iloc`（位置）
print(df.loc[df.index[:3], ['A','B','C']])
print('==========================')
print(df[df.A>8])