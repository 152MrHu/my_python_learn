class Student:
    def __init__(self, weight):
        self.weight= weight

    def run(self):
        self.weight -= 0.5
    def eat(self):
        self.weight += 1
if __name__ == "__main__":
    s1 = Student(150)
    print(s1.weight)
    s1.run()
    print(s1.weight)
