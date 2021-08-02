import StudentController

s = StudentController.StudentController()
student = s.create('小明', 14, '男', 8)

student_list = []
student_list = s.addStudent(student, student_list)
print(student_list)

