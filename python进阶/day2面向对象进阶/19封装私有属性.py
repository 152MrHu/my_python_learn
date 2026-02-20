
# 私有属性  __+名字   只能在类内使用
class Person:
    def __init__(self, name, age):
        self.__name = name  # 私有属性
        self.__age = age    # 私有属性

    def __get_name(self):  # 私有方法
        return self.__name

    def get_age(self):   # 公共方法，访问私有属性
        return self.__age


class Prentice:
    def __init__(self):
        self.kongfu = "[黑马煎饼果子配方]"
        self.__money = 10000  # 私有属性
    def make_cake(self):
        print(f"运用{self.kongfu}  制作煎饼果子")
    def get_money(self):  # 公共方法，访问私有属性
        return self.__money
    def set_money(self, money):  # 公共方法，修改私有属性
        self.__money = money
class TuSun(Prentice):
    pass

if __name__ == '__main__':
    t = TuSun()
    t.make_cake()
    print(t.kongfu)
    # print(t.__money)  # 报错，无法访问私有属性
    print(t.get_money())  # 通过公共方法访问私有属性