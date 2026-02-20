t1 = (1,2,"asd")
t2 = (1,)
t3 = (1)#写逗号
t4 = ()
t5 = tuple()
print(type(t1)) # <class 'tuple'>
print(type(t2)) # <class 'tuple'>
print(type(t3)) # <class 'int'>
print(type(t4)) # <class 'tuple'>
print(type(t5)) # <class 'tuple'>

# 元组嵌套
t6 = (1,2,"asd",(3,4,5),[6,7,8])
print(t6) # (1, 2, 'asd', (3, 4, 5), [6, 7, 8])
# 下标取值
print(t6[3]) # (3, 4, 5)
print(t6[3][0]) # 3
# 无法改变值
# t6[0] = 100 # TypeError: 'tuple' object does not support item assignment

#