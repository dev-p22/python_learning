
class Student:
    language = "Gujarati"  # this attribute associate with class rather than object

    def __init__(self, name , score): # dunder method(that method start from __ score) which is automatically called
        print("I am calling object")
        self.name = name
        self.score = score
    def getInfo(self):
        print(f"The language is {self.language}")

    @staticmethod # this is static method tht don't need self object to pass on.
    def greet():
        print("Good Morning....")    


xyz = Student("xyz",80) # here dunder method will call when we make object
print(xyz.language , xyz.name , xyz.score)
yxz = Student("kitty",29)
yxz.name = "yxz" # Here name is object attribute ans language is class atribute
print(yxz.language , yxz.name)


xyz.getInfo() # Student.getInfo(xyz) it called like that in back
xyz.greet()

