class Student:
    'This class defines a Student for Mechatronics Department'
    department='Mechatronics'
    offSubjects=['Mech','LA','ES','CP-II','MOM','Proj']
    allStudents=[]
   
    def __init__(self,fName,lName,reg):
        self.fName=fName
        self.lName=lName
        self.reg=reg
        self.email=f'{self.reg.lower()}@uet.edu.pk'
        self.courses=['Proj']
        Student.allStudents.append(self)
   
    @property
    def fullName(self):
        return f'{self.fName} {self.lName}'
    def __repr__(self):
        return f'{self.lName}-{self.reg[-2:]}'
    
    def registerSubject(self,*sub):
        for s in sub:
            if s not in Student.offSubjects:
                raise ValueError(f'{s} is not offered!')
            if s not in self.courses:
                self.courses.append(s)
    @classmethod
    def notRegSub(cls):
        "depende de atribuos de la clase, como allStudents, offSubjects, etc. "
        a=set()
        for std in cls.allStudents:
            s=set(std.courses)
            a.update(s)
        return list(set(cls.offSubjects).difference(a))
    
    @staticmethod
    def test(a):
        " No depende de atribuos de la clase. "
        return a**3




            











