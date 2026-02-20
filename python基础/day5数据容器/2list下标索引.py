

name_list = ['张三', '李四', '王五', '赵六']
print(name_list[0]) # 张三
print(name_list[1]) # 李四
# 从右到左-1 -- -2
print(name_list[-1]) # 王五
print(name_list[-2]) # 赵六


list = [[1,2],["asd","ddd"],3,4,5,6,7]
print(list[0]) # [1,2]
print(list[0][0]) # 1
print(list[1][1])
print(list[4]) # 3

# 弄一个三层嵌套
list2 = [[1,2],["asd","ddd"],[3,4,[5,6,7]],8,9]
print(list2[2]) # [3,4,[5,6,7]]
print(list2[2][2]) # [5,6,7]
print(list2[2][2][0]) # 5