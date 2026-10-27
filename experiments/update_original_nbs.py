# -*- coding: utf-8 -*-
import os
import nbformat

root = r'C:\Users\34684\Documents\notes-for-deep-learniung'
mapping = {
    '数据处理笔记.ipynb': (
        '前置基石一：张量操作与特征预处理',
        '对应《西瓜书》第 1 章特征空间与第 11 章特征工程，联动绘本案例课 [`notebooks/01_夏日挑瓜记_偏差方差与双下降曲线.ipynb`](./notebooks/01_夏日挑瓜记_偏差方差与双下降曲线.ipynb)'
    ),
    '线代笔记.ipynb': (
        '前置基石二：矩阵几何、范数与特征谱分解',
        '对应《西瓜书》第 3 章法方程、第 6 章核矩阵正定性与第 10 章 PCA 降维，联动绘本案例课 [`notebooks/04_撑起楚河汉界的少数派_SVM对偶与核技巧案例.ipynb`](./notebooks/04_撑起楚河汉界的少数派_SVM对偶与核技巧案例.ipynb)'
    ),
    '积分导数笔记.ipynb': (
        '前置基石三：多元微积分、梯度与泰勒展开',
        '对应《西瓜书》第 5 章神经网络梯度下降与第 8 章 GBDT/XGBoost 函数空间泰勒展开，联动绘本案例课 [`notebooks/05_三个臭皮匠的数学秘密_随机森林与GBDT残差接力.ipynb`](./notebooks/05_三个臭皮匠的数学秘密_随机森林与GBDT残差接力.ipynb)'
    ),
    '自动求导笔记.ipynb': (
        '前置基石四：PyTorch 动态计算图与反向传播 (Autograd)',
        '对应《西瓜书》第 5 章 5.3 节误差逆传播 (BP) 算法，联动手搓 Autograd 绘本案例课 [`notebooks/06_盲人摸象与回声追责_EM软聚类与手搓Autograd引擎.ipynb`](./notebooks/06_盲人摸象与回声追责_EM软聚类与手搓Autograd引擎.ipynb)'
    ),
    '线性神经网络.ipynb': (
        '核心枢纽五：从高斯/拉普拉斯极大似然到线性神经网络',
        '对应《西瓜书》第 3 章线性模型与第 7 章极大似然估计。本笔记末尾推导的“拉普拉斯噪声在驻点处震荡”已在绘本案例课 [`notebooks/02_天价金瓜搅局记_L1与L2损失及Lasso稀疏几何.ipynb`](./notebooks/02_天价金瓜搅局记_L1与L2损失及Lasso稀疏几何.ipynb) 中完成可视化实验验证！'
    ),
    '线性回归的实现.ipynb': (
        '核心枢纽六：从零手写数据迭代器、小批量 SGD 与线性回归训练闭环',
        '对应《西瓜书》第 3 章最小二乘优化与现代深度学习训练标准范式，联动绘本案例课 [`notebooks/01_夏日挑瓜记_偏差方差与双下降曲线.ipynb`](./notebooks/01_夏日挑瓜记_偏差方差与双下降曲线.ipynb)'
    )
}

for fname, (title, desc) in mapping.items():
    p = os.path.join(root, fname)
    nb = nbformat.read(p, as_version=4)
    header = f"> **《西瓜书 × 深度学习》绘本笔记体系导航** | **{title}**\n> {desc} | 返回主绘本目录：[`README.md`](./README.md)\n\n---"
    if not nb.cells or '绘本笔记体系导航' not in nb.cells[0].source:
        nb.cells.insert(0, nbformat.v4.new_markdown_cell(header))
        nbformat.write(nb, p)
        print("Updated header:", fname)
