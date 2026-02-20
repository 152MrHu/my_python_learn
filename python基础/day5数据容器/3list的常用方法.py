

lst = [1,2,3,4,5,6,3,8,9]
# 判断元素是否在列表中
print(5 in lst) # True
# 查找元素下标 找不到报错
print(lst.index(3)) # 2
#修改元素
lst[0] = 10
print(lst) # [10,2,3,4,5,6,3,
# 插入 元素 下标不存在在末尾插入
lst.insert(1,20)
print(lst) # [10,20,2,3,4,5,6,3,8,9]
# append在末尾添加元素
lst.append(100)
print(lst) # [10,20,2,3,4,5,6, 3,8,9,100]
# extend
lst2 = [200,300,400]
lst.extend(lst2)
print(lst) # [10,20,2,3,4,5,6,3,8,9,100,200,300,400]
# 删除元素del 和pop
del lst[0]
print(lst) # [20,2,3,4,5,6,3,8,9,100,200,300,400]
a = lst.pop(0)
print(a)
print(lst) # [2,3,4,5,6,3,8,9,100,200,300,400]
# remove 删除指定元素第一个
lst.remove(3)
print(lst) # [2,4,5,6,3,8,9,100,200,300,400]
# clear 清空列表
lst.clear()
print(lst) # []
# count 统计元素出现的次数
lst3 = [1,2,3,4,5,6,3,8,9]
print(lst3.count(3)) # 2
# len 统计列表长度
print(len(lst3)) # 9


