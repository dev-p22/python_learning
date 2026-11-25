class Employee:
    a = 1
    @classmethod # it will show class atribute rather than instance attribute. cls jo class jish par method chal raha hein
    def show(cls): 
        print(f"The Value of a is {cls.a}") # here is calling instance attribute



e = Employee()
e.a = 23; # this is override class attribute 
e.name = "xyz"
print(e.name)
e.show() 