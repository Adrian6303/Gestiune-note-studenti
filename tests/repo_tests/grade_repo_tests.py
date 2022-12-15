import unittest

from domain.entities import Student, PbLaborator, Grade
from exceptions.exceptions import GradeAlreadyAssignedException
from repository.grade_repo import GradeFileRepo



class TestCaseGradeRepoFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = GradeFileRepo('test_grade_repo.txt')

    def test_store(self):
        student = Student(567354, 'Marian Faru', 2)
        pbLab = PbLaborator('2_77', 'ceva nou', '5 februarie')

        grade = Grade(567354, '2_77', 3.8)

        self.__repo.store(grade)

        self.assertEqual(len(self.__repo.get_all()), 1)
        self.assertRaises(GradeAlreadyAssignedException, self.__repo.store, grade)

    def test_find(self):
        student1 = Student(744563, 'Leonardo Vrajitorul', 10)
        student2 = Student(679456, 'Felix', 7)

        pbLab1 = PbLaborator('4_89', 'vywgorcnehokcbdygwr', '24 martie')
        pbLab2 = PbLaborator('5_6', 'ceva', '1 mai')

        grade1 = Grade(744563, '4_89', 3.8)
        grade2 = Grade(679456, '5_6', 2.5)

        self.__repo.store(grade1)
        self.__repo.store(grade2)

        grade3 = Grade(744563, '5_6', 4.2)

        self.assertEqual(self.__repo.find(grade1), grade1)
        self.assertIs(self.__repo.find(grade3), None)

    def tearDown(self) -> None:
        self.__repo.delete_all()
