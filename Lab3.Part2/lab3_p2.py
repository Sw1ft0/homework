class Course:
    def __init__(self, name, teacher, course_program):
        self.name = name
        self.teacher = teacher
        self.course_program = course_program

    def __str__(self):
        return f"{self.name} ({self.teacher.name}): {self.course_program}"


class Teacher:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def __str__(self):
        courses_str = "\n".join([str(course) for course in self.courses])
        return f"{self.name}\n{courses_str}"


class LocalCourse(Course):
    def __init__(self, name, teacher, lab, course_program):
        super().__init__(name, teacher, course_program)
        self.lab = lab

    def __str__(self):
        return f"{self.name} ({self.teacher.name}, {self.lab}): {self.course_program}"


class OffsiteCourse(Course):
    def __init__(self, name, teacher, town, course_program):
        super().__init__(name, teacher, course_program)
        self.town = town

    def __str__(self):
        return f"{self.name} ({self.teacher.name}, {self.town}): {self.course_program}"


class CourseFactory:
    def create_local_course(self, name, teacher, lab, course_program):
        return LocalCourse(name, teacher, lab, course_program)

    def create_offsite_course(self, name, teacher, town, course_program):
        return OffsiteCourse(name, teacher, town, course_program)

    def create_teacher(self, name):
        return Teacher(name)


course_factory = CourseFactory()
teacher = course_factory.create_teacher("John Smith")
local_course = course_factory.create_local_course("Java 101", teacher, "Lab 1", "Intro to Java programming")
offsite_course = course_factory.create_offsite_course("Python 202", teacher, "New York", "Intermediate Python programming")
teacher.courses.append(local_course)
teacher.courses.append(offsite_course)

print(teacher)
