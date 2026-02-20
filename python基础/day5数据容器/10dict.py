
dic = {1:"hello",2:9,3:"python","asd":"xxx"}
print(dic) # {1: 'hello', 2: 9, 3: 'python', 'asd': 'xxx'}
#重复会覆盖
dic2 = {1:"hello",2:9,3:"python","asd":"xxx",1:"world"}
print(dic2) # {1: 'world', 2: 9, 3: 'python', 'asd': 'xxx'}

dict1 = {}
dict2 = dict()

print(dic[1])
print(dic["asd"])
# key 不可以为字典 其他都可以
# dic3 = {[1,2,3]:"hello"} # TypeError: unhashable type: 'list'
dic3 = {(1,2,3):"hello"}

# values 可以为字典
dic4 = {1:{1:"hello",2:9,3:"python","asd":"xxx"}}
print(dic4) # {1: {1: 'hello', 2: 9, 3: 'python', 'asd': 'xxx'}}
print(dic4[1][1]) #
