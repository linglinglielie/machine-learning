
from sklearn.neighbors import KNeighborsClassifier
x_train=[[0],[1],[2],[3]]
y_train=[0,0,1,1]
x_test=[[5]]
estimator=KNeighborsClassifier(n_neighbors=3)
estimator.fit(x_train,y_train)
y_pre=estimator.predict(x_test)
print(f"预测的值为{y_pre}")