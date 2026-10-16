import pandas as pd
df = pd.read_csv(r".\示例数据.csv")
print(df.describe())          # 数值列统计
print("==========================================================================")
print(df.describe(include="all"))  # 所有列统计
# 单独数值列统计
print("====数值列描述统计====")
print(df.describe())

# 单独分类文本列统计
print("===文本列描述统计====")
print(df.describe(include=['string','object']))

