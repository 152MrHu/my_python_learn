# 模块的from导入
# from 模块 import 函数/变量/类
from random import randint
from time import time as t
from math import *   # 导入math模块中的所有函数/变量/类
# 使用from导入后，可以直接使用函数/变量/类，无需模块名作为前缀
print(randint(1, 100)) # 生成1-100之间的随机整数
print (t())
print(pi) # 3.141592653589793