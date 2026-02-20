# all默认是*
# from 模块名 import * 只能导入__all__列表中的内容
__all__ = ["wangwang", "hi"]

def wangwang():
    print("a旺旺")

def hi():
    print("hello")

def info():
    print("这是一个自定义模块")
