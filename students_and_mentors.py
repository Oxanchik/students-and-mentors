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

# Testing:
if __name__ == "__main__":
    print("Задание № 1. Наследование:\n")
    lecturer = Lecturer('Иван', 'Иванов')
    reviewer = Reviewer('Пётр', 'Петров')
    print(isinstance(lecturer, Mentor)) # True
    print(isinstance(reviewer, Mentor)) # True
    print(lecturer.courses_attached)    # []
    print(reviewer.courses_attached)    # []