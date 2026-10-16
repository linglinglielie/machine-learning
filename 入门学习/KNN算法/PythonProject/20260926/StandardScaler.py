
from sklearn.preprocessing import StandardScaler
#通过公式吧各列的值映射到均值为0 标准差为1 的正态分布序列
x_train=[[90,2,10,40],[60,4,15,45],[75,3,13,46]]
#创建标准化对象
transfer=StandardScaler()
x_train_new=transfer.fit_transform(x_train)
print("归一化后的数据为:\n")
print(x_train_new)
print(f'数据集的均值为：{transfer.mean_}')#_区分
print(f'数据集的方差为：{transfer.var_}')  #var()
print(f'数据集的标准差为：{transfer.scale_}')#std()