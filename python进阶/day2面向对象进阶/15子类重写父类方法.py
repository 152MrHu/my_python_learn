# 优先调用子类属性和方法
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
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = "[独创配方]"
    def make_cake(self):
        print(f"采用{self.kongfu}  摊煎饼果子")


if __name__ == '__main__':
    p = Prentice()
    print(p.kongfu)
    p.make_cake()