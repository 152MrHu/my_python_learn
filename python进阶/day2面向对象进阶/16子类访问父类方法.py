# 优先调用子类属性和方法
class Master:
    def __init__(self):
        self.kongfu = "[古法配方]"
    def make_cake(self):
        print(f"采用{self.kongfu}  摊煎饼果子Mster")
class School:
    def __init__(self):
        self.kongfu = "[黑马配方]"
    def make_cake(self):
        print(f"采用{self.kongfu}  摊煎饼果子School")
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = "[独创配方]"
    def make_cake(self):
        print(f"采用{self.kongfu}  摊煎饼果子Prentice")
    def make_cake_master(self):
        Master.__init__(self)  # 调用父类的构造方法，重置子类属性
        Master.make_cake(self)


if __name__ == '__main__':
    p = Prentice()
    print(p.kongfu)
    p.make_cake_master()
    print(p.kongfu)
    p.make_cake()
