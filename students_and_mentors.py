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

# Testing:
if __name__ == "__main__":
    # print("Задание № 1. Наследование:\n")
    # lecturer = Lecturer('Иван', 'Иванов')
    # reviewer = Reviewer('Пётр', 'Петров')
    # print(isinstance(lecturer, Mentor)) # True
    # print(isinstance(reviewer, Mentor)) # True
    # print(lecturer.courses_attached)    # []
    # print(reviewer.courses_attached)    # []

    print("Задание № 2. Атрибуты и взаимодействие классов:\n")
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
