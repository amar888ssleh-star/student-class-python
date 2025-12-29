class Student:
    not_allowed_names = ["hell","shit","baloot"]
    users_count=0
    def __init__(self,first_name,middle_name,last_name,gender):
        self.fname=first_name
        self.mname=middle_name
        self.lname=last_name
        self.gender=gender
        Student.users_count += 1
    def fullname(self):
        if self.fname in Student.not_allowed_names:
            print("name not allowed")
        else:
            return f"{self.fname} {self.mname} {self.lname}"

    def delete_user(self):
        Student.users_count -= 1
        return f"user {self.fname} deleted."




    def name_with_title(self):
        if   self.gender =="male":
            return f" Hello Mr {self.fname}"
        elif self.gender =="female":
            return f" Hello Mrs {self.fname}"
        else:
            return f"{self.fname}"
    def get_all_info(self):
        return f"{self.name_with_title()} your full name is {self.fullname()}"


print(Student.users_count)
Student_1=Student("islam","ali","elsaid","male")
Student_2=Student("mona","elsaid","ali","female")
Student_3=Student("amar","elsaid","ali","mhr")
Student_4=Student("shit","hell","metal","ddr")
print(Student.users_count)
print(Student_4.delete_user())
print(Student.users_count)

print(Student_1.get_all_info())
print(Student_2.get_all_info())
print(Student_3.get_all_info())
print(Student_4.get_all_info())
#print(dir(Student))
