
t1 = (1,2,3,4,5)
# index查找
print(t1.index(3)) # 2
# print(t1.index(8))  报错

# count计数
t2 = (1,2,3,4,5,3,3)
print(t2.count(3)) # 3

# 元组里套list可以修改
t3 = (1,2,3,[4,5,6])
t3[3][0] = 100
print(t3) # (1, 2, 3, [100, 5, 6])
#list整体不能改
# t3[3] = [100,200,300] # TypeError: 'tuple' object does not support item assignment


for x in t1:
    print(x) # 1 2 3 4 5