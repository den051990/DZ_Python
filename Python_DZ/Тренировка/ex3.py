from student import Student
from course_group import CourseGroup

student = Student("Денис", "Денисов", 20, "Информатика")
classmate1 = Student("Сергей", "Сергеев", 22, "Информатика")
classmate2 = Student("Марк", "Марков", 21, "Информатика")
classmate3 = Student("Максим", "Максимов", 23, "Информатика")

course_group = CourseGroup(student, [classmate1, classmate2, classmate3])
print(course_group)