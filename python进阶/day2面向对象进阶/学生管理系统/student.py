class Student:
    def __init__(self, name,gender , age, phone, desc):
        """
        初始化学生信息
        :param name:   学生姓名
        :param gender:  学生性别
        :param age:   学生年龄
        :param phone:   学生联系电话
        :param desc:   学生描述信息
        """
        self.name = name
        self.gender = gender
        self.age = age
        self.phone = phone
        self.desc = desc
    def __str__(self):
        return f"Student(name={self.name}, gender={self.gender}, age={self.age}, phone={self.phone}, desc={self.desc})"

# 测试
if __name__ == '__main__':
    s1 = Student("Alice", "Female", 20, "1234567890", "A diligent student")
    s2 = Student("Bob", "Male", 22, "0987654321", "An excellent student")
    print(s1)
    print(s2)