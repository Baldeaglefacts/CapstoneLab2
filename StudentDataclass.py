from dataclasses import dataclass


@dataclass
class Student:  # defines student class. Includes what information will be saved about students
    name: str
    college_id: int
    gpa: float

    def __str__(self):  # handles formatting for when printing student information
        return f'{self.name}. ID: {self.college_id}. GPA: {self.gpa}'


def main():  # adds example students

    alice = Student('Alice', 12345, 3.5)
    bob = Student('Bob', 98765, 3.6)

    print(alice)
    print(bob)


main()

# Using dataclasses makes it easier and cleaner looking when defining variables. The traditional method
# requires wordier code (self.name = name, compared to name = str). It's also easier to tell what a variable is
# (Str, int, float, ect) at a glance.
