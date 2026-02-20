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
# 父类中有重复的属性或者方法用第一个父类的
s1 = Son()
print(s1.gender)
s1.walk()


class Master:
    def __init__(self):
        self.kongfu = "[古法配方]"
    def make_cake(self):
        print(f"采用{self.kongfu}  摊煎饼果子")
class School:
    def __init__(self):
        self.kongfu = "[黑马配方]"
    def make_cake(self):
        print(f"采用{self.kongfu}  摊煎饼果子")
class Prentice(School,Master):
    pass

p = Prentice()
print(p.kongfu)
p.make_cake()

# MRO方法解析顺序  先找子类  再找父类  父类有多个时按照继承顺序找
print(Prentice.mro()) # [<class '__main__.Prentice'>, <class '__main__.School'>, <class '__main__.Master'>, <class 'object'>]