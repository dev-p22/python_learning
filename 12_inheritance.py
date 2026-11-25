class Subject():
    def __init__(self,subject):
        self.subject = subject
    def showSubject(self):
       print(f"The name of subject is : {self.subject}")


class Student(Subject):
    def __init__(self,name , marks,subject):
        super().__init__(subject)
        self.name = name
        self.marks = marks
    def showStudent(self):
        print(f"The name of student is : {self.name} and marks is : {self.marks} of {self.subject}" )


phy = Subject("physics")
maths = Subject("Maths")
guj = Subject("Gujarati")
xyz = Student("xyz",79,phy.subject)
xyz = Student("xyz",73,guj.subject)

phy.showSubject()
maths.showSubject()
guj.showSubject()
xyz.showStudent()
xyz.showStudent()


