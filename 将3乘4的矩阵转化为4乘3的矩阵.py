matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# 方法一
list1 = [[row[i] for row in matrix] for i in range(4)]
print(list1)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# 方法二
list2 = []
for i in range(4):
    list2.append([row[i] for row in matrix])
print(list2)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# 方法三
list3 = []
for i in range(4):
    list3_row =[]
    for row in matrix:
        list3_row.append(row[i])
    list3.append(list3_row)
print(list3)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
