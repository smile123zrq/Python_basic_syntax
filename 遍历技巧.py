# 遍历一个序列的两种方式
list1 = list(range(10))
# 方法1，直接遍历
for i in list1:
    print(i, end='  ')
print('\n')
# 方法2，按索引遍历
for i in range(len(list1)):
    print(list1[i], end='  ')
print('\n')


# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():  # 结果为：gallahad the pure
    print(k, v)                      # robin the brave


# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v, end="   ")      # 结果为：0 tic   1 tac   2 toe

print('\n')


# 同时遍历两个或更多的序列，可以使用 zip() 组合
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
'''
运行结果为：
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
'''

# 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数
for i in reversed(questions):       # 不会改变原序列的值
    print(i, end='  ')

print('\n')
# 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f, end='  ')
