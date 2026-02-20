
"""
面向对象进阶-对象属性和类属性
对象属性：每个对象独有的属性，定义在__init__方法中
类属性：所有对象共享的属性，定义在类体中 ，函数外 修改只能通过类名修改
对象属性优先级高于类属性，如果对象和类都有同名属性，访问对象属性会覆盖类属性
可以通过对象访问类属性，但不能通过类访问对象属性
"""
class Student:
    # 类属性
    school = "ABC University"

    def __init__(self, name, age):
        # 对象属性
        self.name = name
        self.age = age
    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, school={self.school})"


if __name__ == '__main__':
    s1 = Student("Alice", 20)
    s2 = Student("Bob", 22)
    print(s1)  # Student(name=Alice, age=20, school=ABC University)
    Student.school = "XYZ University"  # 修改类属性
    print(s1)
    print(s2)
    s1.school = "PQR University"  # 只修改s1的school属性，创建了一个新的对象属性
    print(s1)  # Student(name=Alice, age=20, school=PQR
    print(s2)  # Student(name=Bob, age=22, school=XYZ University)

