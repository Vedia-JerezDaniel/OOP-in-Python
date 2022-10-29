from myClasses import Student

std1=Student('Anwar','Ali','MCT-UET-01') 
std2=Student('Akbar','Khan','MCT-UET-02')
std3=Student('Hamza','Akhtar','MCT-UET-03')

std1.registerSubject('CP-II','MOM','MOM')
std1.department = "Electronics"

help(std1)

# print(std1.fullName)

std2.reg = "SAK_W2"
print(std2.email)
std3.reg = "Han_G2"
print(std3.email)

std1.fName = "Mammed"
print(std1.fullName)

for i in std1.__dict__.items():
    print(i)
print(15*'-')
for i in std2.__dict__.items():
    print(i)
