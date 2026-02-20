s = set()
print(type(s)) # <class 'set'>
s2 = {}
print(type(s2)) # <class 'dict'>

s1 = {3,7,1,2,4,5,1,4,5}
print(s1) # {1, 2, 3, 4, 5} 去重了 无序

# 无下标，可修改，不可重复
s1.add(6)
print(s1) # {1, 2, 3, 4, 5, 6}
s1.add(1)
print(s1) # {1, 2, 3, 4, 5, 6} 没有重复的1
# 移除指定元素
s1.remove(2)
print(s1) # {1, 3, 4, 5, 6}

# pop随机移除一个元素
s1.pop()
print(s1) # {3, 4, 5, 6} 随机移除一个元素

# 清空集合
s1.clear()

# 集合取交集
s2 = {1,2,3,4,5}
s3 = {4,5,6,7,8}
print(s2 & s3) # {4, 5} 交集
print(s2.intersection(s3)) # {4, 5} 交集

# 集合取并集
print(s2)
print(s3)
print(s2 | s3)
print(s2.union(s3)) # {1, 2, 3, 4, 5, 6, 7, 8} 并集

# 集合取差集
print(s2)
print(s3)
print(s2 - s3) # {1, 2, 3} 差集
print(s2.difference(s3)) # {1, 2, 3}

# 集合差集消除 difference_update
print(s2)
print(s3)
print(s2.difference_update(s3))


# 遍历只能用for
for i in s2:
    print(i)

# 可以混装
s4 = {1,2,3,"hello",True}
print(s4) # {1, 2, 3, 'hello', True}