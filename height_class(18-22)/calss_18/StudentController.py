import Student


class StudentController:

    def create(self, name, age, sex, class_num):
        s = Student.Student()
        s.setName(name)
        s.setAge(age)
        s.setSex(sex)
        s.setClass(class_num)
        return s

    def addStudent(self, student, student_list):
        student_list.append(student)
        return student_list

    def removeStudent(self, num, student_list):
        del student_list[num]
        return student_list

    def resetStudent(self, student, num, student_list):
        student_list[num] = student

