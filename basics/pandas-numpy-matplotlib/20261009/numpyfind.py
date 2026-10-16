import numpy as np
a=np.arange(3,15)
print(a)
print(a[3])
print('=======二维里输出')
b=np.arange(3,15).reshape((3,4))
print(b)
print(b[2])#索引行数
print(b[1][1])#索引一个准确值
print(b[1,1])#同样索引值
print(b[2,:])#索引第二行所有数
print(b[:,1])#索引第一列的值
print(b[1,1:2])#索引·第一行第一位到第二位的值
print('====================================================')
print(b)
for row in b:
    print(row)#遍历行
print('==============================')
for column in b.T:
    print(column)#转置后能遍历列
    print('=====================================')
    print(b)
    print(b.flatten())
    print('=====================================')
    for item in b.flat:
        print(item)