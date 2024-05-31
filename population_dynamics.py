import numpy as np
import matplotlib.pyplot as plt

# 查找系统中可用的字体
from matplotlib import font_manager

# 设置字体，假设已经安装了 SimHei 字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False    # 解决保存图像时负号 '-' 显示为方块的问题

# 构造阶段矩阵A
A = np.array([[0, 1.6],
              [0.3, 0.8]])

# 初始种群向量
x_0 = np.array([[15],
                [10]])

# 演化k年后的种族向量
x_k = x_0

# 画图的传入的列表
x1 = []
x2 = []
y = []
# x3是总数量, x4是成年数量和幼年数量每年的比率
x3 = []
x4 = []

n = int(input('输入演化的年数n:'))
for num in range(n + 1):
    x1.append(x_k[1, 0])
    x2.append(x_k[0, 0])
    x3.append(x_k[1, 0] + x_k[0, 0])
    if x_k[0, 0] != 0:
        x4.append(x_k[1, 0] / x_k[0, 0])
    else:
        x4.append(0)  # 防止除以零
    y.append(num)
    x_k = A @ x_k  # 演化一年

# 打印 x4 的数据
print("成年数量和幼年数量每年的比率:", x4)

# 创建图形
# 注意此处应为 y 对应年份, x 对应成年数量
plt.plot(y, x1, label='成年数量')
plt.plot(y, x2, label='幼年数量')
plt.plot(y, x3, label='总数量')
plt.plot(y, x4, label='成年数量和幼年数量每年的比率')

# 创建标签和标题
plt.title('成年数量随年份的变化图')
plt.xlabel('演化的年份')
plt.ylabel('动物的数量')

# 添加图例
plt.legend()

plt.show()
