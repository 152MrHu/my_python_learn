from 学生管理系统.student import Student

s1 = Student("Alice", "Female", 20, "1234567890", "A diligent student")
print(s1)

print("*"*34)
# 把学生对象转换成字典
my_dic = s1.__dict__             #——————————————————
print(my_dic)
print(type(my_dic))

print("*"*34)
# 把    [学生对象.学生对象.学生对象]   转成    [字典.字典.字典]

stu_list = [s1,s1,s1]
stu_dict = [stu.__dict__ for stu in stu_list]
print(stu_dict)

print("*"*34)
# 字典转成对象
my_dic = s1.__dict__
s2 = Student(**my_dic)   #_____________________
print(s2)

