# Numpy中使用astype函数将指定数组转化为和另外一个数组相同的数据类型
import numpy as np

x = np.array([-1.0, 1.0, 2.0])
print(x)
'''
[-1.  1.  2.]
'''

y = x > 0
print(y)
'''
[False  True  True]
对NumPy数组进行不等号运算后，数组的各个元素都会进行不等号运算，
生成一个布尔型数组。这里，数组x中大于0 的元素被转换为True，小于等
于0 的元素被转换为False，从而生成一个新的数组y。
'''

y = y.astype(int)
print(y)
'''
[0 1 1]
数组y是一个布尔型数组，但是我们想要的阶跃函数是会输出int型的0
或1 的函数。因此，需要把数组y的元素类型从布尔型转换为int型。
如上所示，可以用astype()方法转换NumPy数组的类型。astype() 方
法通过参数指定期望的类型，这个例子中是int型。Python 中将布尔型
转换为int型后，True会转换为1，False会转换为0。以上就是阶跃函数的
实现中所用到的NumPy的“技巧”。
'''
