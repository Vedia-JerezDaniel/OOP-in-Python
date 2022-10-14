class Student:

    def __init__(self,fName,lName,reg,phone):
        self.fName=fName
        self.lName=lName
        self.reg=reg
        self.email=f'{self.reg.lower()}@uet.edu.pk'
        self.phone=phone

    def welcome(self):
        return f'Welcome {self.fName} {self.lName} to OOP in Python'

## Main Program ##
std1=Student('Anwar','Ali','MCT-UET-01','6262') # Object Instantiated and Initialzed
std2=Student('Akbar','Khan','MCT-UET-02','8060')

print(std1.welcome())
print(std2.welcome())

print(std1.phone)

