# OOP Model: Students, Lecturers, Reviewers

This project implements a simple object-oriented model of an educational process in Python.  
It includes **students**, **lecturers**, and **reviewers** with grading logic, average grade calculation, and comparison of objects by their average scores.

---

## Features

- `Student` can:
    - Receive homework grades
    - Rate `Lecturer` for courses in progress
    - Be compared to other students by average homework grade

- `Lecturer` can:
    - Receive lecture grades from students
    - Be compared to other lecturers by average lecture grade

- `Reviewer` can:
    - Rate students’ homework for courses they are attached to

- Common functionality:
    - Calculation of average grade for a person (`avg_grade`)
    - Average grade for a specific course among all students (`avg_students_grade`)
    - Average grade for a specific course among all lecturers (`avg_lecturers_grade`)
    - Comparison logic is shared via a mixin `ComparableByAvgGradeMixin`

---

## Class Overview


### `ComparableByAvgGradeMixin`

_This mixin allows to reuse the logic of comparing the average rating 
in several classes (for example, Student and Lecturer), avoiding code duplication._

<br>

### `Student`
**Inherits from:** `ComparableByAvgGradeMixin`

***Stores:***

- _name, surname, gender_
- _finished_courses (list)_
- _courses_in_progress (list)_
- _grades (dict[str, list[int]])_

<br>

***Methods:***

- `rate_lecture(lecturer, course, grade)` - rate a lecturer (grade 1–10)
- Comparison operators (`==`, `!=`, `<`, `<=`, `>`, `>=`) via mixin
- `__str__` for pretty printing student info

<br>

### `Mentor`

***Stores:***

- _name, surname_
- _courses_attached (list)_

<br>

### `Lecturer`

**Inherits from:** `Mentor` and `ComparableByAvgGradeMixin`

***Stores:***

- _grades (dict[str, list[int]])_

<br>

***Methods:***

- Can be rated by students
- Comparison operators (`==`, `!=`, `<`, `<=`, `>`, `>=`) via mixin
- `__str__` for pretty printing lecturer info

<br>

### `Reviewer`

**Inherits from:** `Mentor`

***Methods:***

- `rate_hw(student, course, grade)` - rate student's homework (grade 1–10)
- `__str__` for pretty printing reviewer info

<br>

### Grade Calculation Functions

`avg_grade(course_grades: dict) -> float`
*Calculates average grade across all courses for one person. 
Returns 0.0 if course_grades dictionary is empty or contains no grades at all.*

`avg_students_grade(students_list: list, course_name: str) -> float`
*Calculates average grade for a specific course among all students.*

*Ignores objects that:*

- *Are not Student instances*
- *Don't have valid grades dictionary*
- *Don't contain the specified course*

`avg_lecturers_grade(lecturers_list: list, course_name: str) -> float`
*Similar to avg_students_grade, but for lecturers (Lecturer instances).*

___
## Requirements
- Python 3.10+
- No external dependencies required
