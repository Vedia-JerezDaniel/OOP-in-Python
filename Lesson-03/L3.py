class Student:
    department=['Mechatronics']
    offSubjects=['Mech','LA','ES','CP-II','MOM','Proj']

    def __init__(self,fName,lName,reg,phone):
        self.fName=fName
        self.lName=lName
        self.reg=reg
        self.email=f'{self.reg.lower()}@uet.edu.pk'
        self.phone=phone
        self.courses=['Proj']
    
    def registerSubject(self, *sub):
        for s in sub:
            if s not in Student.offSubjects:
                raise ValueError(f'Course: {s} is not offered!')
            if s not in self.courses:
                self.courses.append(s)
            if s in ['LA', 'ES']:
                print(f'{s} is not in {Student.department}')    

            

## Main Program ##
std1=Student('Anwar','Ali','MCT-UET-01',5612)
std2=Student('Akbar','Khan','MCT-UET-02',6600)
std3=Student('Hamza','Akhtar','MCT-UET-03',8521)

std1.registerSubject('CP-II','MOM','MOM')
std2.registerSubject('LA', 'CP-II')
std3.registerSubject('Mech','MOM')

print(std1.courses)
print(std2.courses)
print(std3.courses)










