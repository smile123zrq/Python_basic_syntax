# 格式化字符串的函数 str.format(),基本语法是通过 {} 和 : 来代替以前的 % 。
# format 函数可以接受不限个参数，位置可以不按顺序。
print('{} {}'.format('Hello', 'World!'))  # 不设置指定位置，按默认位置排序
print('{0} {1}'.format('Hello', 'World!'))  # 设置指定位置
print('{0} {1} {0}'.format('Hello', 'World!'))  # 设置指定位置
'''
Hello World!
Hello World!
Hello World! Hello
'''


# 设置参数
print('网站名：{name},地址：{url}'.format(name='牛客网', url='www.newcode.com'))
# 网站名：牛客网,地址：www.newcode.com

# 通过字典设置参数
x = {'name': '牛客网', 'url': 'www.newcode.com'}
print('网站名:{name},地址：{url}'.format(**x))    # 字典名前面要加两个*
# 网站名：牛客网,地址：www.newcode.com

# 通过列表索引设置参数
my_list = ['牛客网', 'www.newcode.com']
my_list2 = ['Hello', 'World!']
# 这里的0或1是指format参数中的列表，是用来指定是哪一个列表的，不能省略
print('网站名：{0[0]}，地址：{0[1]}'.format(my_list))  # 0是必须要写的
print('网站名：{0[0]}，地址：{0[1]},第二个列表测试{1[0]} {1[1]}'.format(my_list, my_list2))

# 数字格式化
# 详细格式看网址：https://www.nowcoder.com/tutorial/10004/f7cf4da35e194775a4dd77b17c1fa193
# 保留小数位数
print('保留两位小数：{:.2f}'.format(3.14159))
print('保留4位小数：{:.4f}'.format(3.14159))
# 带符号保留小数
print('保留两位小数：{:+.2f}'.format(3.14159))  # 输出结果为：保留两位小数：+3.14
# 以逗号分隔数字格式
print('每三位分隔：{:,}'.format(1000000))  # 输出结果为：每三位分隔：1,000,000
# 百分比格式
print('百分比格式：{:.3%}'.format(0.25))  # 输出结果为：百分比格式：25.000%
# 科学计数法，指数格式
print('指数格式:{:.2e}'.format(10000000))   # 输出结果为：指数格式:1.00e+07
