"""
创建类的格式
class 类名(父类1, 父类2, ...):
    类体

"""
# 所有类都默认继承object类
class Father:
    def __init__(self):
        self.gender = "男"

    def walk(self):
        print(f"饭后走一走,身体更健康")
class Mother:
    def __init__(self):
        self.gender = "女"
    def walk(self):
        print(f"饭后走一走")

class Son(Mother,Father):
    pass


s1 = Son()
print(s1.gender)
s1.walk()