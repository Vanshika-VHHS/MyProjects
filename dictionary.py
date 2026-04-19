student_dict = {"name" : "Dheeraj", "number": 717 , "grade": 7}
#print(student_dict)

# Using dict() constructor
#employee=dict(eno=1,ename="Deheeraj")
#print(employee)

employer=dict(eno=2,ename="Dheeraj")
employer.update(ename="Dheeraj vedantham")
#print(employer)
new=dict(student_dict,**employer)
print(new)

