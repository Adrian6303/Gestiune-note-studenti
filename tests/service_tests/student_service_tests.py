import unittest

from domain.validators import Validator
from exceptions.exceptions import ValidationException, StudentNotFoundException
from repository.student_repo import StudentFileRepo
from service.student_service import StudentService


class TestCaseStudentService(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = StudentFileRepo('test_e_student_service.txt')
        validator = Validator()
        self.__srv = StudentService(self.__repo, validator)

    def test_add_student(self):
        added_student = self.__srv.add_student(112199, 'Frank', 7)
        self.assertTrue(added_student.getNume() == 'Frank')
        self.assertTrue(added_student.getGrup() == 7)

        self.assertEqual(len(self.__srv.get_all_students()), 1)
        self.assertRaises(ValidationException, self.__srv.add_student, 452, 'Frank', 9)

    def test_delete_student(self):
        self.__srv.add_student(112199, 'Frank', 7)
        deleted_student = self.__srv.delete_student(112199)

        self.assertEqual(len(self.__srv.get_all_students()), 0)
        self.assertEqual(deleted_student.getNume(), 'Frank')
        self.assertEqual(deleted_student.getGrup(), 7)
        self.assertRaises(StudentNotFoundException, self.__srv.delete_student, 895624)

    def test_get_all_students(self):
        self.__srv.add_student(112199, 'Frank', 7)
        self.__srv.add_student(689022, 'Horner', 8)
        self.assertIsInstance(self.__srv.get_all_students(), list)
        self.assertEqual(len(self.__srv.get_all_students()), 2)

    def test_edit_student(self):
        self.__srv.add_student(112199, 'Frank', 7)
        updated_student = self.__srv.edit_student(112199, 'Frank cel Mare', 9)

        self.assertTrue(updated_student.getNume() == 'Frank cel Mare')
        self.assertTrue(updated_student.getGrup() == 9)
        self.assertRaises(StudentNotFoundException, self.__srv.edit_student, 795621, 'Frank cel Mare', 9)

    def tearDown(self) -> None:
        self.__repo.delete_all()


if __name__ == '__main__':
    unittest.main()
