# 导入包
import math
import matplotlib.pyplot as plt
# 计算正弦值
x_start = 0 # 弧度值
print(math.sin(x_start))
x_end = 2*math.pi # 弧度值
print(math.sin(x_end))
# 等差数列 a_n = a_1 + d(n – 1)
# 数列元素数量
num = 37
# 计算公差
step = (x_end - x_start) / (num - 1) 
# 生成等差数列列表
x_array = [x_start + i * step for i in range(num)]
# 生成等长全0列表,等价于zero_array = [0] * len(x_array)
zero_array = [0 for i in range(num)]
y_array = [math.sin(x_idx) for x_idx in x_array]
# 可视化正弦函数
plt.plot(x_array, y_array, marker = '.',
 markersize = 8,
 markerfacecolor="w",
 markeredgecolor='k')
plt.text(x_start, -0.1, '0')
plt.text(x_end, 0.1, r'$2\pi$')
plt.axhline(y=0, color='k', linestyle='--', linewidth=0.25)
plt.axis('off')
plt.show()