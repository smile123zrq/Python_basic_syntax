# choice(seq)方法返回一个列表，元组或字符串的随机项。seq -- 可以是一个列表，元组或字符串。
import random
a = [1, 2, 3, 4, 5, 6]
print(random.choice(a))
print(random.choice('HelloWorld!'))
print(random.choice(range(101)))

# randrange ([start,] stop [,step]),返回指定递增基数集合中的一个随机数，基数默认值为1。
# start -- 指定范围内的开始值，包含在范围内。
# stop -- 指定范围内的结束值，不包含在范围内。
# step -- 指定递增基数。
print('从0到100中随机选取一个奇数：', random.randrange(1, 101, 2))
print('从0到100中随机选取一个偶数：', random.randrange(0, 101, 2))
print('从0到100中随机选取一个数：', random.randrange(101))

# random() 方法返回随机生成的一个实数，它在[0,1)范围内。
print('第一个随机数：', random.random())
print('第二个随机数：', random.random())

# shuffle(lst) 方法将序列的所有元素随机排序。参数：lst -- 列表。
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst)
random.shuffle(lst)
print(lst)

# uniform(x, y)方法将随机生成下一个实数，它在 [x,y] 范围内。
print("uniform(5, 10) 的随机浮点数 : ", random.uniform(5, 10))
print("uniform(7, 14) 的随机浮点数 : ", random.uniform(7, 14))

'''
随机数函数：choice(seq)   返回seq中随机的一个元素，seq可以是列表，元组或字符串 random.choice(seq)
          randrange(x, y, z)从指定的范围[x,y)随机返回一个整数，z为步长 random.randrange(x, y, z)
          random()      返回[0,1)内的一个随机浮点数 random.random()
          shuffle(lst)  将列表lst中的元素随机排序 random.shuffle(lst)
          uniform(x, y) 返回在[x,y]内的一个随机浮点数 random.uniform(x, y)
'''