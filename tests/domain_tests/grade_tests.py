import unittest

from domain.validators import Validator

from domain.entities import Student, PbLaborator, Grade
from exceptions.exceptions import ValidationException


class TestCaseGradeDomain(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = Validator()

    def test_create_grade(self):
        student = Student(895176, 'Randunica Adriana', 12)
        pbLab = PbLaborator('2_7', 'Cautare numere prime', '5 martie')

        grade = Grade(895176, '2_7', 4.1)

        self.assertEqual(grade.getStudent(), 895176)
        self.assertEqual(grade.getPbLab(), '2_7')
        self.assertEqual(grade.getGrade(), 4.1)

    def test_equal_grade(self):
        student = Student(895176, 'Randunica Adriana', 12)
        pbLab = PbLaborator('2_7', 'Cautare numere prime', '5 martie')

        grade1 = Grade(895176, '2_7', 4.1)
        grade2 = Grade(895176, '2_7', 4.5)

        self.assertEqual(grade1, grade2)

        student2 = Student(578102, 'Marinache Iberiu', 4)
        grade3 = Grade(578102, '2_7', 3)
        self.assertNotEqual(grade3, grade2)

    def test_grade_validator(self):
        student = Student(578102, 'Marinache Iberiu', 4)
        pbLab = PbLaborator('2_7', 'Cautare numere prime', '5 martie')

        grade = Grade(578102, '2_7', 4)

        self.__validator = Validator()
        self.__validator.validate_grade(grade)

        grade1 = Grade(student, pbLab, 100)
        self.assertRaises(ValidationException, self.__validator.validate_grade, grade1)
