import numpy as np
a=np.array([1,1,1])
b=np.array([2,2,2])
print(np.vstack((a,b)))
print('===================================')
c=np.vstack((a,b))#vertical stack
print(c)
print(c.shape,a.shape)
print('=======================================')
d=np.hstack((a,b))#horizontal stack左右合并
print(d)
print(a.shape,d.shape)
print('=======================================')
print(a.T)#结果证明不能把一个横向的序列变成一个竖向的矩阵
print('================')
print(a[np.newaxis,:].shape)
print(a[np.newaxis,:])
print(a[:,np.newaxis].shape)
print(a[:,np.newaxis])
print('============')
A=np.array([1,1,1])[:,np.newaxis]
B=np.array([2,2,2])[:,np.newaxis]
print(np.hstack((A,A,B)))
c=np.concatenate((A,B,A),axis=0)#在列上合并
print(c)