import unittest

from domain.validators import Validator
from exceptions.exceptions import GradeAlreadyAssignedException, StudentNotFoundException, PbLabNotFoundException, \
    ValidationException
from repository.pbLab_repo import PbLabFileRepo
from repository.grade_repo import GradeFileRepo
from repository.student_repo import StudentFileRepo
from service.grade_service import GradeService


class TestCaseGradeService(unittest.TestCase):
    def setUp(self) -> None:
        student_repo = StudentFileRepo('test_student_service.txt')
        pbLab_repo = PbLabFileRepo('test_pbLab_service.txt')

        self.__initialize_grades_file()

        grade_repo = GradeFileRepo('test_grade_service.txt')
        val = Validator()

        self.__srv = GradeService(student_repo, pbLab_repo, grade_repo, val)

    def __initialize_grades_file(self):
        with open("original_grades.txt", 'r') as f:
            with open("test_grade_service.txt", "w") as f1:
                f1.write(f.read())

    def test_create_grade(self):
        created_grade = self.__srv.create_grade(567354, '2_77', 8)

        self.assertEqual(created_grade.getStudent(), 567354)
        self.assertEqual(created_grade.getPbLab(), '2_77')
        self.assertEqual(created_grade.getGrade(), 8)

        self.assertRaises(GradeAlreadyAssignedException, self.__srv.create_grade, 567354, '2_77', 8)
        self.assertRaises(StudentNotFoundException, self.__srv.create_grade, 571255, '2_77', 3)
        self.assertRaises(PbLabNotFoundException, self.__srv.create_grade, 567354, '6_6', 4.8)
        self.assertRaises(ValidationException, self.__srv.create_grade, 785613, '5_6', 96.0)

    def test_get_avg_sub5(self):
        exist = self.__srv.get_avg_sub5()
        self.assertEqual(exist, True)

    def test_stat_studenti_note(self):
        exist = self.__srv.stat_studenti_note(679456)
        self.assertEqual(exist, False)

    def test_get_media_max(self):
        exist = self.__srv.get_media_max()
        self.assertEqual(exist, 'Studentul:  Leonardo Vrajitorul  cu media:  9.0')


if __name__ == '__main__':
    unittest.main()
