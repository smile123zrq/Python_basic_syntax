x = 100
# 将x转换为一个整数
a = int(x)
print(type(a), a)

# 将x转换成一个浮点数
b = float(x)
print(type(b), b)

# 将x转化为一个复数
c = complex(x)
print(type(c), c)    # 此函数将x转化为实数部分，虚数部分为0。complex(x,y) x为实数部分，y为虚数部分

# 将x转化为字符串
d = str(x)
print(type(d), d)

# 将元组转化成列表
e = (1, 2, 3, 4, 5)
print(type(e))
print(type(list(e)))

# 将列表转化为元组
f = [1, 2, 3, 4, 5]
print(type(f))
print(type(tuple(f)))

# chr(x) 将一个整数转化为一个字符
# ord(x) 将一个字符转化为它的整数值
# hex(x) 将一个整数转化为一个十六进制字符串
# oct(x) 将一个整数转化为一个八进制字符串
