def swap(a):
    c = a[0]
    a[0] = a[1]
    a[1] = c


x = list(input('请输入两个数字：'))
print(x)
swap(x)
print(x)
