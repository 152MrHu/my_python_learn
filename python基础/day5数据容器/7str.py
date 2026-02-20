# 字符串下标操作
s = 'hello world'
print(s[0]) # h
print(s[1]) # e
print(s[-1]) # d
print(s[-2]) # l
# 字符串修改
# s[0] = 'H' # TypeError: 'str' object does not support item assignment
# index
print(s.index('o')) # 4
print(s.index("ll"))

# replace替换
s2 = s.replace("o","O")
print(s2) # hellO wOrld

# split分割 存入list
s3 = s.split(" ")
print(s3) # ['hello', 'world']
print(type(s3)) # <class 'list'>

# strip去除空格和回车 返回一个新字符串
s4 = "  hello world  "
print(s4.strip()) # hello world
print(s4.strip(" ")) # hello world

# count计数
s5 = "hello world hello"
print(s5.count("hello")) # 2

# len长度
print(len(s5)) # 17