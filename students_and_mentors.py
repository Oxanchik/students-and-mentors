class Student:
    """Student class.
    Can receive grades for homework.
    Can evaluate lecturers.

    Properties:
        name (str): Student's first name (read-only).
        surname (str): Student's last name (read-only).
        gender (str): Student's gender (read-only).

    Attributes:
        finished_courses (list): List of completed courses.
        courses_in_progress (list): List of ongoing courses.
        grades (dict): Dictionary with grades received for each course.

    Methods:
        rate_lecture: Evaluates lecturer for courses in progress.

    """

    def __init__(self, name: str, surname: str, gender: str):
        """Initialize a new student instance.

        Args:
            name (str): Student's first name.
            surname (str): Student's last name.
            gender (str): Student's gender ('М' or 'Ж').

        """
        if not isinstance(name, str):
            raise TypeError(f"Name must be str, not {type(name).__name__}")
        if not isinstance(surname, str):
            raise TypeError(f"Surname must be str, not {type(surname).__name__}")
        if not isinstance(gender, str):
            raise TypeError(f"Gender must be str, not{type(gender).__name__}")

        if gender.strip().upper() not in ["М", "Ж"]:
            raise ValueError(f"Gender must be 'М' or 'Ж'")

        self._name = name.strip().title()
        self._surname = surname.strip().title()
        self._gender = gender.strip().upper()
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    @property
    def name(self) -> str:
        """Get student's first name."""
        return self._name

    @property
    def surname(self) -> str:
        """Get student's last name."""
        return self._surname

    @property
    def gender(self) -> str:
        """Get student's gender."""
        return self._gender

    def rate_lecture(self, target_lecturer, course: str, grade: int):
        """Rate lecturer for a specific course.

        Args:
            target_lecturer: Lecturer being rated.
            course: Course name.
            grade: Grade to assign (0-10).

        Returns:
            str: 'Ошибка' if the operation is invalid, None on success.

        """
        if (isinstance(target_lecturer, Lecturer) and
                course in self.courses_in_progress and
                course in target_lecturer.courses_attached and
                0 <= grade <= 10):
            if course in target_lecturer.grades:
                target_lecturer.grades[course] += [grade]
            else:
                target_lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self) -> str:
        """Returns student's information."""
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade(self.grades):.2f}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __eq__(self, other) -> bool:
        """Equal: student1 == student2 (by average rating)"""
        if not isinstance(other, Student):
            return NotImplemented
        return avg_grade(self.grades) == avg_grade(other.grades)

    def __ne__(self, other) -> bool:
        """Not equal: student1 != student2 (by average rating)"""
        if not isinstance(other, Student):
            return NotImplemented
        return avg_grade(self.grades) != avg_grade(other.grades)

    def __lt__(self, other) -> bool:
        """Less than: student1 < student2 (by average rating)"""
        if not isinstance(other, Student):
            return NotImplemented
        return avg_grade(self.grades) < avg_grade(other.grades)

    def __le__(self, other) -> bool:
        """Less than or equal: student1 <= student2 (by average rating)"""
        if not isinstance(other, Student):
            return NotImplemented
        return avg_grade(self.grades) <= avg_grade(other.grades)

    def __gt__(self, other) -> bool:
        """Greater than: student1 > student2 (by average rating)"""
        if not isinstance(other, Student):
            return NotImplemented
        return avg_grade(self.grades) > avg_grade(other.grades)

    def __ge__(self, other) -> bool:
        """Greater than or equal: student1 >= student2 (by average rating)"""
        if not isinstance(other, Student):
            return NotImplemented
        return avg_grade(self.grades) >= avg_grade(other.grades)


class Mentor:
    """Parent class for all mentors.
    Stores basic info about the mentor.

    Attributes:
        _name (str): The mentor's first name.
        _surname (str): The mentor's last name.
        courses_attached (list): List of courses the mentor is responsible for.

    """

    def __init__(self, name: str, surname: str):
        """Initialize a new mentor instance.

        Args:
            name (str): Mentor's first name.
            surname (str): Mentor's last name.

        """
        if not isinstance(name, str):
            raise TypeError(f"Name must be str, not {type(name).__name__}")
        if not isinstance(surname, str):
            raise TypeError(f"Surname must be str, not {type(surname).__name__}")

        self._name = name.strip().title()
        self._surname = surname.strip().title()
        self.courses_attached = []

    @property
    def name(self) -> str:
        """Get mentor's name."""
        return self._name

    @property
    def surname(self) -> str:
        """Get mentor's surname."""
        return self._surname


class Lecturer(Mentor):
    """Lecturer class for mentors. Can give lectures and be evaluated by students.
    Inherited from the parent class Mentor.

    Notes:
        - This subclass extends the __init__ method from Mentor
          to include additional attributes for Lecturer specifics.
        - Any methods defined in this class will complement those inherited
          from Mentor, but none will override Mentor's core functionalities.

    """

    def __init__(self, name: str, surname: str):
        """Initialize a new lecturer instance."""
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self) -> str:
        """Returns lecturer's information."""
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade(self.grades):.2f}")

    def __eq__(self, other) -> bool:
        """Equal: lecturer1 == lecturer2 (by average rating)"""
        if not isinstance(other, Lecturer):
            return NotImplemented
        return avg_grade(self.grades) == avg_grade(other.grades)

    def __ne__(self, other) -> bool:
        """Not equal: lecturer1 != lecturer2 (by average rating)"""
        if not isinstance(other, Lecturer):
            return NotImplemented
        return avg_grade(self.grades) != avg_grade(other.grades)

    def __lt__(self, other) -> bool:
        """Less than: lecturer1 < lecturer2 (by average rating)"""
        if not isinstance(other, Lecturer):
            return NotImplemented
        return avg_grade(self.grades) < avg_grade(other.grades)

    def __le__(self, other) -> bool:
        """Less than or equal: lecturer1 <= lecturer2 (by average rating)"""
        if not isinstance(other, Lecturer):
            return NotImplemented
        return avg_grade(self.grades) <= avg_grade(other.grades)

    def __gt__(self, other) -> bool:
        """Greater than: lecturer1 > lecturer2 (by average rating)"""
        if not isinstance(other, Lecturer):
            return NotImplemented
        return avg_grade(self.grades) > avg_grade(other.grades)

    def __ge__(self, other) -> bool:
        """Greater than or equal: lecturer1 >= lecturer2 (by average rating)"""
        if not isinstance(other, Lecturer):
            return NotImplemented
        return avg_grade(self.grades) >= avg_grade(other.grades)


class Reviewer(Mentor):
    """Reviewer class for mentors. Can evaluate the students.
    Inherited from the parent class Mentor.

    Notes:
        - This subclass extends the __init__ method from Mentor
          to include additional attributes for Reviewer specifics.
        - Any methods defined in this class will complement those inherited
          from Mentor, but none will override Mentor's core functionalities.

    """

    def __init__(self, name, surname):
        """Initialize a new reviewer instance."""
        super().__init__(name, surname)

    def rate_hw(self, target_student, course: str, grade: int):
        """Rate a student's homework for a specific course.

        Args:
            target_student (Student): Student being rated.
            course (str): Course name.
            grade (int): Grade to assign (0-10).

        Returns:
            str: 'Ошибка' if the operation is invalid, None on success.

        Notes:
            - A mentor can rate homework only for students currently taking
              the same course as the mentor.
            - Grades are stored as lists inside the student's `grades` dictionary.

        """
        if (isinstance(target_student, Student) and
                course in self.courses_attached and
                course in target_student.courses_in_progress and
                0 <= grade <= 10):
            if course in target_student.grades:
                target_student.grades[course] += [grade]
            else:
                target_student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        """Returns reviewer's information."""
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")


def avg_grade(course_grades: dict) -> float:
    """Calculate average grade for one person courses.

    Args:
        course_grades (dict): Dictionary with course names as keys and lists of grades as values.

    Returns:
        float: Average grade across all courses or 0.0 if no grades.

    """
    if not course_grades:
        return 0.0

    target_rating = []
    for grades in course_grades.values():
        target_rating.extend(grades)

    if not target_rating:
        return 0.0

    return sum(target_rating) / len(target_rating)

def avg_students_grade(students_list: list, course_name: str) -> float:
    """Calculate average grade for a particular course among all students.

    Args:
        students_list (list): List of students for a partucular course.
        course_name (str): Course name.

    Returns:
        float: Average grade for the course across all students or 0.0 if no grades.

    """
    target_rating = []
    for student in students_list:
        if course_name in student.grades:
            target_rating.extend(student.grades[course_name])

    if not target_rating:
        return 0.0

    return sum(target_rating) / len(target_rating)

def avg_lecturers_grade(lecturers_list: list, course_name: str) -> float:
    """Calculate average grade for a particular course among all lecturers.

    Args:
        lecturers_list (list): List of lecturers for a partucular course.
        course_name (str): Course name.

    Returns:
        float: Average grade for the course across all students or 0.0 if no grades.

    """
    target_rating = []
    for lecturer in lecturers_list:
        if course_name in lecturer.grades:
            target_rating.extend(lecturer.grades[course_name])

    if not target_rating:
        return 0.0

    return sum(target_rating) / len(target_rating)

# Testing:
if __name__ == "__main__":
    print("Задание № 1. Наследование:\n")
    lecturer = Lecturer('Иван', 'Иванов')
    reviewer = Reviewer('Пётр', 'Петров')
    print(isinstance(lecturer, Mentor)) # True
    print(isinstance(reviewer, Mentor)) # True
    print(lecturer.courses_attached)    # []
    print(reviewer.courses_attached)    # []

    print("\n\nЗадание № 2. Атрибуты и взаимодействие классов:\n")
    lecturer = Lecturer('Иван', 'Иванов')
    reviewer = Reviewer('Пётр', 'Петров')
    student = Student('Ольга', 'Алёхина', 'Ж')

    student.courses_in_progress += ['Python', 'Java']
    lecturer.courses_attached += ['Python', 'C++']
    reviewer.courses_attached += ['Python', 'C++']

    print(student.rate_lecture(lecturer, 'Python', 7))   # None
    print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
    print(student.rate_lecture(lecturer, 'С++', 8))      # Ошибка
    print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка

    print(lecturer.grades)  # {'Python': [7]}

    print("\n\nЗадание № 3. Полиморфизм и магические методы и Задание № 4. Полевые испытания:\n")
    reviewer1 = Reviewer('Василий', 'Иванов')
    reviewer1.courses_attached += ['Java', 'Python', 'Git', 'OOP']
    reviewer2 = Reviewer('Григорий', 'Волков')
    reviewer2.courses_attached += ['Python', 'Git', 'OOP']
    lecturer1 = Lecturer('Сергей', 'Петров')
    lecturer1.courses_attached += ['Python', 'Java', 'OOP']
    lecturer2 = Lecturer('Вера', 'Васильева')
    lecturer2.courses_attached += ['Git', 'OOP', 'Python']
    student1 = Student('Николай', 'Степанов', 'М')
    student2 = Student('Лидия', 'Зайцева', 'М')
    student1.finished_courses += ['C++', 'Java']
    student1.courses_in_progress += ['Python', 'Git', 'OOP']
    student1.rate_lecture(lecturer1, 'Python', 8)
    student1.rate_lecture(lecturer2, 'Git', 9)
    student1.rate_lecture(lecturer2, 'Python', 9)
    student2.finished_courses += ['Git', 'Java']
    student2.courses_in_progress += ['Python', 'OOP', 'C++']
    student2.rate_lecture(lecturer1, 'Python', 9)
    student2.rate_lecture(lecturer1, 'OOP', 8)
    student2.rate_lecture(lecturer2, 'Python', 8)
    reviewer1.rate_hw(student1, 'Python', 8)
    reviewer1.rate_hw(student1, 'OOP', 7)
    reviewer1.rate_hw(student2,'Python', 8)
    reviewer1.rate_hw(student2, 'OOP', 8)
    reviewer2.rate_hw(student1, 'Python', 9)
    reviewer2.rate_hw(student1, 'OOP', 7)
    reviewer2.rate_hw(student2,'Python', 9)
    reviewer2.rate_hw(student2, 'OOP', 8)

    print("Проверяющие:\n")
    print(reviewer1, "\n")
    print(reviewer2, "\n")
    print("\nЛекторы:\n")
    print(lecturer1, "\n")
    print(lecturer2, "\n")
    print("\nСтуденты:\n")
    print(student1, "\n")
    print(student2, "\n")

    print("\nТестирование операторов сравнения\n")
    print("Сравнение студентов по средней оценке:")
    print(f"{student1.name} {student1.surname}, средняя оценка: {avg_grade(student1.grades):.2f}")
    print(f"{student2.name} {student2.surname}, средняя оценка: {avg_grade(student2.grades):.2f}")
    print(f"{student1.name} {student1.surname} == {student2.name} {student2.surname}: {student1 == student2}")
    print(f"{student1.name} {student1.surname} != {student2.name} {student2.surname}: {student1 != student2}")
    print(f"{student2.name} {student2.surname} < {student2.name} {student2.surname}: {student1 < student2}")
    print(f"{student1.name} {student1.surname} > {student2.name} {student2.surname}: {student1 > student2}")
    print(f"{student1.name} {student1.surname} <= {student2.name} {student2.surname}: {student1 <= student2}")
    print(f"{student1.name} {student1.surname} >= {student2.name} {student2.surname}: {student1 >= student2}")
    print("\nСравнение лекторов по средней оценке:")
    print(f"{lecturer1.name} {lecturer1.surname}, средняя оценка: = {avg_grade(lecturer1.grades):.2f}")
    print(f"{lecturer2.name} {lecturer2.surname}, средняя оценка:  = {avg_grade(lecturer2.grades):.2f}")
    print(f"{lecturer1.name} {lecturer1.surname} == {lecturer2.name} {lecturer2.surname}: {lecturer1 == lecturer2}")
    print(f"{lecturer1.name} {lecturer1.surname} != {lecturer2.name} {lecturer2.surname}: {lecturer1 != lecturer2}")
    print(f"{lecturer1.name} {lecturer1.surname} < {lecturer2.name} {lecturer2.surname}: {lecturer1 < lecturer2}")
    print(f"{lecturer1.name} {lecturer1.surname} > {lecturer2.name} {lecturer2.surname}: {lecturer1 > lecturer2}")
    print(f"{lecturer1.name} {lecturer1.surname} <= {lecturer2.name} {lecturer2.surname}: {lecturer1 <= lecturer2}")
    print(f"{lecturer1.name} {lecturer1.surname} >= {lecturer2.name} {lecturer2.surname}: {lecturer1 >= lecturer2}")

    print("\nСредняя оценка курсов:")
    course1 = 'OOP'
    course2 = 'Python'
    print(f"Средняя оценка за домашние задания у студентов курса {course1}: {avg_students_grade([student1, student2], course1):.2f}")
    print(f"Средняя оценка за лекции у лекторов курса {course2}: {avg_lecturers_grade([lecturer1, lecturer2], course2):.2f}")

    print("\nСортировка студентов по средней оценке:")
    students_sorted = sorted([student1, student2], reverse=True)
    for i, target_student in enumerate(students_sorted, 1):
        print(f"{i}. {target_student.name} {target_student.surname}: {avg_grade(target_student.grades):.2f}")

    print("\nСортировка лекторов по средней оценке:")
    lecturers_sorted = sorted([lecturer1, lecturer2, lecturer], reverse=True)
    for i, target_lecturer in enumerate(lecturers_sorted, 1):
        print(f"{i}. {target_lecturer.name} {target_lecturer.surname}: {avg_grade(target_lecturer.grades):.2f}")