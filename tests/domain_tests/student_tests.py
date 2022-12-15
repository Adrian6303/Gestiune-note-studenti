import unittest

from domain.entities import Student
from domain.validators import Validator
from exceptions.exceptions import ValidationException


class TestCaseStudentDomain(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = Validator()

    def test_create_student(self):
        student1 = Student(578102, 'Marinache Iberiu', 4)
        self.assertEqual(student1.getStudentID(), 578102)
        self.assertEqual(student1.getNume(), 'Marinache Iberiu')
        self.assertEqual(student1.getGrup(), 4)

        student1.setStudentID(567123)
        student1.setNume('Pasare Valeriu')
        student1.setGrup(7)

        self.assertEqual(student1.getStudentID(), 567123)
        self.assertEqual(student1.getNume(), 'Pasare Valeriu')
        self.assertEqual(student1.getGrup(), 7)

    def test_equals_student(self):
        student1 = Student(895176, 'Randunica Adriana', 12)
        student2 = Student(895176, 'Randunica Adriana', 12)

        self.assertEqual(student1, student2)

        student3 = Student(128626, 'Randunica Adriana', 12)
        self.assertNotEqual(student1,student3)

    def test_student_validator(self):
        student1 = Student(578102, 'Marinache Iberiu', 4)
        self.__validator.validate_student(student1)
        student2 = Student(578102, '', 4)
        student3 = Student(578102, 'Marinache Iberiu', -4)

        self.assertRaises(ValidationException, self.__validator.validate_student, student2)
        self.assertRaises(ValidationException, self.__validator.validate_student, student3)
