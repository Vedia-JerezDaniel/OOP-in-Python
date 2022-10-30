from myClasses import Student

std1=Student('Anwar','Ali','MCT-UET-01') 
std2=Student('Akbar','Khan','MCT-UET-02')
std3=Student('Hamza','Akhtar','MCT-UET-03')
std4=Student('Faisal','Iqbal','MCT-UET-04')

std1.setGroupMember(std2)

print(f'{std1.fName} group member with: {std1.groupMember}')

print(std3.groupMember)

print(Student.withoutGroupMembers())




