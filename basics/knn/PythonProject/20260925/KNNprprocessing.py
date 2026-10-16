from sklearn.neighbors import KNeighborsRegressor
#差值(3,11,9) (2,10,10) (0,1,0) (1,0,2）
#平方和 211    204        1        5
#开根号 14.53   14.28     1        2.24
#临近值现在为三,如果为四的话，那么一直为0.25.
#K值过小，易受异常值影响，会导致模型学到大量的脏特征，致使 过拟合
#K值过大，模型变简单，致使欠拟合

x_train=[[0,0,1],[1,1,0],[3,10,10],[4,11,12]]#训练集的特征数据，因为特征可以有多个特征，所以是二维数组
y_train=[0.1,0.2,0.3,0.4]#训练集的标签数据，因为标签连续，所以是一维数组
x_test=[[3,11,10]]#二维数组！！
estimator=KNeighborsRegressor(n_neighbors=3)
estimator.fit(x_train,y_train)
y_pred=estimator.predict(x_test)
print(f'预测结果是：{y_pred}')