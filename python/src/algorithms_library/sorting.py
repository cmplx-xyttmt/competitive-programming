from operator import itemgetter, attrgetter
from typing import List, Tuple

if __name__ == '__main__':
    student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10)
    ]

    # sorting using lambda functions
    print(sorted(student_tuples, key=lambda student: student[2]))

    # sorting using operator module functions (itemgetter(), attrgetter(), methodcaller())
    print(sorted(student_tuples, key=itemgetter(2)))

    # operators allow multiple levels of sorting. E.g sorting by the second element and then the third
    print(sorted(student_tuples, key=itemgetter(1, 2)))

    # sorting in descending order
    print(sorted(student_tuples, key=itemgetter(2), reverse=True))

    # multi-sort: e.g sort by grade, then by age
    class Student:

        def __init__(self, name, grade, age):
            self.name = name
            self.grade = grade
            self.age = age

        def __repr__(self):
            return repr((self.name, self.grade, self.age))

    student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10)
    ]

    def multisort(xs: List[Student], specs: List[Tuple[str, bool]]):
        for key, reverse in reversed(specs):
            xs.sort(key=attrgetter(key), reverse=reverse)
        return xs

    print(multisort(list(student_objects), [('grade', True), ('age', False)]))
