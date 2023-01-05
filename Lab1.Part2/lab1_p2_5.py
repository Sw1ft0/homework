class Student:

    def __init__(self,
                 name: str,
                 surname: str,
                 number: int,
                 grades: list):
        for grade in grades:
            if grade < 0 or grade > 100:
                raise ValueError('Invalid grade')
        if not isinstance(number, int):
            raise TypeError('record-book number must be an integer value')
        self.name = name
        self.surname = surname
        self.number = number
        self.grades = grades

    def __str__(self):
        return f"{self.name} {self.surname}"

    def average_grade(self):
        return sum(self.grades)/len(self.grades)


class Group:

    def __init__(self, title: str, limit: int):
        if not isinstance(limit, int):
            raise TypeError('Group limit number must be an integer value')
        self.__title = title
        self.__list = []
        self.limit = limit

    def list_add(self, student: Student):
        if len(self.__list) == self.limit:
            raise ValueError("group can include only 20 students")
        for member in self.__list:
            if (member.name, member.surname) == (student.name, student.surname):
                raise Exception(f"student {student.name} {student.surname} already exists in the group")
        self.__list.append(student)

    def highest_average(self):
        best_students = self.__list[:]

        best_students.sort(key=lambda student: student.average_grade())
        best_students.reverse()
        for student in best_students[:5]:
            print(f"{student.name} {student.surname}", sep="\n")

    def __str__(self):
        return f"{self.__title} {self.__list}"


my_group = Group("TB-12", 20)
my_group.list_add(Student("Pavlo", "Kostianov", 452234, [100, 100, 100]))
my_group.list_add(Student("Ivan", "Kuruch", 452231, [100, 99, 98]))
my_group.list_add(Student("Mykola", "Pylypchuk", 452232, [98, 100, 96]))
my_group.list_add(Student("Olexandr", "Pylypenko", 452233, [78, 67, 87]))
my_group.list_add(Student("Olha", "Nesheret", 452235, [88, 86, 75]))
my_group.list_add(Student("Oleg", "Neresnycia", 452236, [100, 100, 86]))
my_group.list_add(Student("Vlad", "Mashtaler", 452237, [78, 100, 97]))
my_group.list_add(Student("Volodymyr", "Krutygolova", 452238, [68, 69, 76]))

my_group.highest_average()

