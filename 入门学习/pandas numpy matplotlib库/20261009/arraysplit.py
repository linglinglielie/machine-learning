import numpy as np
a=np.arange(2,14).reshape((3,4))
print(a)


print(np.split(a,2,axis=1))                    #对列进行改变，等快分割,不能用这个函数进行不等的分割
print('==============')
print(np.split(a,3,axis=0))
print('===============================')
print(np.array_split(a,3,axis=1))
print('===========================')
print(np.vsplit(a,3))
print(np.hsplit(a,2))