# 导入 NumPy 包
import numpy as np

# 生成 NumPy 数组，np.array() 接收列表作为参数
x = np.array([1.0, 2, 3, 4])
print(x)
print(type(x))
'''
[1. 2. 3. 4.]   这里的这个 . 是小数点的意思，数组里没有分隔符
<class 'numpy.ndarray'>
'''

# NumPy 数组的算术运算，每个数组的元素个数必须相同
# 这里只是数组对应位置元素位置计算，并不是像现代里面那样的矩阵相乘
x = np.array([1.0, 2, 3])
y = np.array([4.0, 5, 6])
print(x + y)  # 对应位置元素相加
print(x - y)  # 对应位置元素相减
'''
[5. 7. 9.]
[-3. -3. -3.]
'''
print(x * y)  # 对应位置元素相乘
print(x / y)  # 对应位置元素相除
print(x * 10)  # x数组中每个元素乘10
print(x / 10)  # x数组中每个元素除10
print(x + 10)  # x数组中每个元素加10
print(x - 10)  # x数组中每个元素减10

# NumPy的N维数组(N维向量)
# 二维数组（矩阵）
A = np.array([[1, 2, 3], [3, 4, 5]])
print(A)
print(A.shape)  # 查看A的形状(几行几列)
'''
[[1 2 3]
 [3 4 5]]
(2, 3)
'''
print(A.dtype)  # 查看矩阵元素的数据类型
# 矩阵的算术运算,跟一维数组的操作一样
B = np.array([[4, 5, 6], [6, 7, 8]])
print(A + B)
print(A * B)
print(A * 10)

# 访问数组元素
X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)
'''
[[51 55]
 [14 19]
 [ 0  4]]
'''
print(X[0])  # 输出3行2列数组的第一行
print(X[0][1])  # 输出第1行第2个元素
'''
[51 55]
55
'''
# 使用for循环遍历数组
for row in X:
    print(row)  # 每次输出一行
'''
[51 55]
[14 19]
[0 4]
'''
# 一个一个输出数组中的元素
for row in X:
    for x in row:
        print(x)

# NumPy 使用数组访问各个元素
X = X.flatten()  # 将X转换为一维数组
print(X)
# [51 55 14 19  0  4]

# 获取索引为 0 2 4 的元素
print(X[np.array([0, 2, 4])])
'''
[51 14  0]

print(X[0, 2, 4])
不能这样写，会报错
'''

# 使用这个标记法，可以获取满足一定条件的元素，例如从X中抽出大于15的元素
print(X > 15)
# [ True  True False  True False False]
print(X[X > 15])    # 输出X中大于15的元素
# [51 55 19]
print(X[0, 2, 4])
