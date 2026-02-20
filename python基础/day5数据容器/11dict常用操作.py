
dic = {1:"hello",3:"python","asd":"xxx"}

# 新增
dic[4] = "java"
print(dic) # {1: 'hello', 3: 'python', 'asd': 'xxx', 4: 'java'}

# 更新
dic[4] = "c++"
print(dic) # {1: 'hello', 3: 'python', 'asd': 'xxx', 4: 'c++'}

# 删除
del dic[4]
print(dic) # {1: 'hello', 3: 'python', 'asd': 'xxx'}
dic.pop(1)
print(dic) # {3: 'python', 'asd': 'xxx'}

# 获取所有的key
print(dic.keys()) # dict_keys([3, 'asd'])

# 遍历
for key in dic.keys():
    print(key) # 3 asd
for key in dic:
    print(key) # 3 asd

# 清空
dic.clear()
print(dic) # {}

