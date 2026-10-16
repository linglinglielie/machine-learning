import pandas as pd
import numpy as np
dates=pd.date_range('20180101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(df)
print(df.fillna(value=0))
df.iloc[2,2]=1111
df.loc['20180102','B']=222
df[df.A>0]=0
print(df)
#df.A[df.A>0]=0#**链式赋值错误**，新版 pandas（2.0+，你现在 Python3.14 配套的 pandas）开启了`Copy-on-Write`写时复制机制，禁止这种写法
df.loc[df.A > 0, 'A'] = 0
df['F']=np.nan
df['E']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20180101',periods=6))
print(df)
print('==========')
