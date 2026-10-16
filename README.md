# 机器学习入门练习

> 本仓库记录机器学习入门学习过程中的练习代码，包含 KNN 算法、NumPy、pandas、matplotlib 等内容，持续更新。

## 仓库结构

```
machine-learning/
├─ basics/                          # 入门学习
│  ├─ knn/                          # KNN 算法
│  │  └─ PythonProject/
│  │     ├─ 20260925/               # KNN 分类器、数据预处理
│  │     └─ 20260926/               # 归一化、标准化
│  └─ pandas-numpy-matplotlib/      # 数据处理三剑客
│     ├─ 20261009/                  # NumPy 基础
│     ├─ 20261010/                  # pandas 基础
│     ├─ 20261013matplotlib/        # matplotlib 入门
│     ├─ 20261014/
│     └─ 20261015/                  # CSV 读取与描述统计
├─ .gitignore
└─ README.md
```

## 学习进度

| 日期 | 主题 | 内容 |
| --- | --- | --- |
| 2026-09-25 | KNN | KNN 分类器、数据预处理 |
| 2026-09-26 | KNN | 最小-最大归一化、标准化、鸢尾花案例 |
| 2026-10-09 | NumPy | 数组创建、连接、分割、查找 |
| 2026-10-10 | pandas | 数据连接、读写、选取、拷贝 |
| 2026-10-13 | matplotlib | 绘图入门 |
| 2026-10-14 | pandas | 函数练习 |
| 2026-10-15 | pandas | CSV 读取、describe 描述统计 |

## 环境说明

- Python 版本：Python 3.x
- 主要库：NumPy、pandas、matplotlib、scikit-learn
- 编辑器：PyCharm

### 运行方式

```bash
python 文件名.py
```

## 每日上传命令

```bash
git add .
git commit -m "日期: 练习内容"
git push
```

## 提交记录格式

- `init:` 初始化仓库
- `knn:` KNN 相关
- `numpy:` NumPy 相关
- `pandas:` pandas 相关
- `matplotlib:` matplotlib 相关
- `refactor:` 重构 / 调整结构
- `docs:` 文档更新

示例：

```bash
git commit -m "pandas: 2026-10-15 describe描述统计练习"
```

## 说明

- 本仓库为个人学习记录，代码仅供参考
- 如有错误欢迎指出，一起学习进步
