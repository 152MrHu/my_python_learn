
"""
多态：同一操作作用于不同的对象，可以有不同的解释，产生不同的执行结果。
多态的前提：继承，方法重写，父类引用指向子类。
多态的体现：父类引用指向子类对象。
多态的好处：提高了代码的扩展性和维护性。
"""
class Animal:  #抽象类(也叫接口)，不能被实例化
    def speak(self):  #抽象方法
        print("动物在叫")

class Dog(Animal):
    def speak(self):
        print("汪汪汪")
class Cat(Animal):
    def speak(self):
        print("喵喵喵")
class Car:
    def speak(self):
        print("汽车在叫")

def make_animal(animal:Animal):
    animal.speak()
an:Animal = Dog() # 父类引用指向子类对象
d = Dog()
c = Cat()
ca = Car()
# 演示多态
make_animal(d)
make_animal(c)
make_animal(ca)  # 这也是多态，虽然car不是Animal的子类，但它也有speak方法，所以也可以调用