#开发流程 加载数据 数据预处理 特征工程 模型训练 评估 预测
# 导入工具包
from sklearn.datasets import load_iris        # 加载鸢尾花测试集的
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split   # 分割训练集和测试集的
from sklearn.preprocessing import StandardScaler      # 数据标准化的
from sklearn.neighbors import KNeighborsClassifier    # KNN算法 分类对象
from sklearn.metrics import accuracy_score             # 模型评估的，计算模型预测的准确率

#1定义函数，加载鸢尾花数据集，并查看数据集
def dm01_load_iris():
    iris = load_iris()
    print("特征名：", iris.feature_names)
    print("标签名：", iris.target_names)
    return iris

#2定义函数，绘制数据集的散点图
def dm02_show_iris():
    iris_data = load_iris()
    #把鸢尾花数据集封装成DataFrame对象
    iris_df=pd.DataFrame(iris_data.data,columns=iris_data.feature_names)
    #给df对象新增1列  标签列
    iris_df['label']=iris_data.target
    #print(iris_df)
    #根据Seaborn绘制散点图
    #参1：数据集，参2：X轴 参3：Y轴 参4：分组字段 参5：是否显示拟合线
    sns.lmplot(data=iris_df,x='sepal length (cm)',y='sepal width (cm)',hue='label',fit_reg=True)
    #设置标题
    plt.title('Iris Data')
    plt.tight_layout()#自动调整了图参数，以使整个图像的边界与子图匹配
    plt.show()
#3定义函数，切分训练集和数据集
def dm03_show_iris():
    iris_data = load_iris()
    #数据预处理，从150个特征和标签中，按照八比二
    #返回值：训练集的特征数据，测试集的特征数据，训练集的标签数据，测试机的标签数据
    #参4：随机种子（种子一致，每次生成的随机数据集都是固定的）
    x_train,x_test,y_train,y_test=train_test_split(iris_data.data,iris_data.target,test_size=0.2,random_state=23)

    #打印分割后的结果
    print(f'训练集的特征：{x_train},个数：{len(x_train)}')
    print(f'训练集的标签：{y_train},个数:{len(y_train)}')
    print(f'测试集的特征:{x_test},个数:{len(x_test)}')
    print(f'测试集的标签：{y_test},个数:{len(y_test)}')
#4定义函数，实现鸢尾花完整案例，加载数据集，数据预处理，特征工程，模型训练，评估，预测
if __name__ == '__main__':
    # dm01_load_iris()
    #dm02_show_iris()
    dm03_show_iris()