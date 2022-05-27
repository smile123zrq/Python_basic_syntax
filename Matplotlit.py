# 导入库
import numpy as np
import matplotlib.pyplot as plt

# 生成数据
x = np.arange(0, 20, 0.1)    # 生成一个一维数组，左并右开，步长为0.1
y = np.sin(x)   # 生成y数组，取值为x数组中的sin值

# 绘制图形
plt.plot(x, y)  # sin函数图像
plt.show()

# pyplot 功能
# 生成数据
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 绘制图形
plt.plot(x, y1, label='sin')
plt.plot(x, y2, linestyle='--', label='cos')    # 用虚线绘制
plt.xlabel('x')     # x轴标签
plt.ylabel('y')     # y轴标签
plt.title('sin & cos')  # 标题
plt.legend()    # 给图加上图例
plt.show()

# 显示图像
'''
pyplot 中还提供了用于显示图像的方法imshow()。另外，可以使用
matplotlib.image模块的imread()方法读入图像
'''
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('3.png')   # 读入图片
plt.imshow(img)
plt.show()




















