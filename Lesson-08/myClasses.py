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
        self.groupMember=None
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
    def setGroupMember(self,mate):
        if(self.groupMember != None):
            raise ValueError(f'{self} already has {self.groupMember} as group member')
        elif(mate.groupMember!=None):
            raise ValueError(f'{mate} already has {mate.groupMember} as group member')
        else:
            self.groupMember=mate
            mate.groupMember=self
    def dropGroupMember(self,mate):
        if self.groupMember is None and mate.groupMember is None:
            return
        elif(self.groupMember!=mate):
            raise ValueError(f'{self} is not group member of {mate}.')
        else:
            self.groupMember=None
            mate.groupMember=None
    
    @classmethod
    def withoutGroupMembers(cls):
        return list(filter(lambda s: s.groupMember is None, cls.allStudents))
   
    @classmethod
    def notRegSub(cls):
        a=set()
        for std in cls.allStudents:
            s=set(std.courses)
            a.update(s)
        return list(set(cls.offSubjects).difference(a))
    




            











