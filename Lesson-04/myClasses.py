class Student:
    'This class defines a Student for Mechatronics Department'
    department='Mechatronics'
    offSubjects=['Mech','LA','ES','CP-II','MOM','Proj']
    
    def __init__(self,fName,lName,reg):
        self.fName=fName
        self.lName=lName
        self.reg=reg
        self.courses=['Proj']
   
    @property
    def email(self):
        return f'{self.reg.lower()}{self.lName.lower()}@uet.edu.pk'
    @property
    def fullName(self):
        return f'{self.fName} {self.lName}'
    

    
    def registerSubject(self,*sub):
        for s in sub:
            if s not in Student.offSubjects:
                raise ValueError(f'{s} is not offered!')
            if s not in self.courses:
                self.courses.append(s)
            











