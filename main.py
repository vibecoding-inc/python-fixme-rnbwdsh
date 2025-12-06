import sys

class Integer:
    """Wrapper class for Integer to mimic Java Integer object."""
    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

class Student:
    """Represents a student entity."""
    def __init__(self, name, grade):
        self._name = name
        self._grade = Integer(grade)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_grade(self):
        return self._grade.get_value()

    def set_grade(self, grade):
        self._grade.set_value(grade)

class GradeCalculator:
    """Service class to handle grade calculations."""
    def __init__(self):
        pass

    def is_passing(self, student):
        """Determines if a student is passing based on a threshold."""
        if student.get_grade() >= 50:
            return True
        else:
            return False

class StudentManager:
    """Manager class to handle a list of students."""
    def __init__(self):
        self._students = []

    def add_student(self, student):
        self._students.append(student)

    def get_students(self):
        return self._students

class Application:
    """Main application entry point."""
    def __init__(self):
        self._manager = StudentManager()
        self._calculator = GradeCalculator()

    def run(self):
        # Initializing data
        names = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
        grades = [85, 42, 60, 49, 90]

        # Populating the manager
        for i in range(len(names)):
            s = Student(names[i], grades[i])
            self._manager.add_student(s)

        # Processing logic
        passing_students = []
        all_students = self._manager.get_students()

        # Explicit index-based loop
        for i in range(len(all_students)):
            current_student = all_students[i]
            if self._calculator.is_passing(current_student) == True:
                passing_students.append(current_student)

        # Calculate Average
        total = 0
        count = 0
        for i in range(len(passing_students)):
            total = total + passing_students[i].get_grade()
            count = count + 1

        average = 0.0
        if count > 0:
            average = total / count

        print("Processing complete.")
        print("Passing Student Count: " + str(count))
        print("Average Grade of Passing Students: " + str(average))

if __name__ == "__main__":
    app = Application()
    app.run()
