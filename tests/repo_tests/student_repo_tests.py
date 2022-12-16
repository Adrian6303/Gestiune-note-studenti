import unittest

from domain.entities import Student
from exceptions.exceptions import DuplicateIDException, StudentNotFoundException
from repository.student_repo import StudentFileRepo


class TestCaseStudentRepoFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = StudentFileRepo('test_student_repo.txt')
        self.__repo.delete_all()
        self.__populate_list()

    def __populate_list(self):
        student1 = Student(567354, 'Marian Faru', 2)
        student2 = Student(679456, 'Felix', 7)
        student3 = Student(744563, 'Leonardo Vrajitorul', 10)
        student4 = Student(785613, 'Franz', 3)
        student5 = Student(963680, 'pbhalh', 24)
        student6 = Student(674563, 'Marius', 4)
        student7 = Student(674224, 'Frederik', 4)
        student8 = Student(556724, 'Marian', 8)
        student9 = Student(676154, 'Modoi', 9)
        student10 = Student(567111, 'Vancea', 12)

        self.__repo.store(student1)
        self.__repo.store(student2)
        self.__repo.store(student3)
        self.__repo.store(student4)
        self.__repo.store(student5)
        self.__repo.store(student6)
        self.__repo.store(student7)
        self.__repo.store(student8)
        self.__repo.store(student9)
        self.__repo.store(student10)

    def test_find(self):
        p = self.__repo.find(567354)
        self.assertTrue(p.getStudentID() == 567354)
        self.assertTrue(p.getNume() == 'Marian Faru')
        self.assertEqual(p.getGrup(), 2)

        p1 = self.__repo.find('111111')
        self.assertIs(p1, None)

    def test_size(self):
        initial_size = self.__repo.size()
        self.__repo.delete(963680)
        self.__repo.delete(674563)

        self.assertEqual(self.__repo.size(), initial_size - 2)

        self.__repo.store(Student(567242, 'Vivaldi', 3))
        self.assertEqual(self.__repo.size(), initial_size - 1)
        self.__repo.edit(785613, Student(785613, '785613', 2))
        self.assertEqual(self.__repo.size(), initial_size - 1)

    def test_get_all(self):
        initial_size = self.__repo.size()
        crt_students = self.__repo.get_all()
        self.assertIsInstance(crt_students, list)

        self.assertEqual(len(crt_students), initial_size)

        self.__repo.delete(674224)
        self.__repo.delete(556724)

        crt_students = self.__repo.get_all()
        self.assertEqual(len(crt_students), initial_size - 2)

        self.__repo.store(Student(678122, 'Goran', 1))
        self.assertTrue(self.__repo.size() == initial_size - 1)

        self.__repo.edit(678122, Student(678122, 'Gropar', 2))

        self.assertTrue(self.__repo.size() == initial_size - 1)

    def test_store(self):
        initial_size = self.__repo.size()
        student1 = Student(511167, 'Norbert', 1)
        self.__repo.store(student1)

        self.assertEqual(self.__repo.size(), initial_size + 1)
        student2 = Student(782811, 'Carl Cox', 6)
        self.__repo.store(student2)
        self.assertEqual(self.__repo.size(), initial_size + 2)
        self.assertRaises(DuplicateIDException, self.__repo.store, student2)

    def test_delete(self):
        initial_size = self.__repo.size()
        student1 = Student(222345, 'Berinde', 15)
        self.__repo.store(student1)
        student2 = Student(676752, 'Elon', 3)
        self.__repo.store(student2)

        deleted_student = self.__repo.delete(222345)
        self.assertTrue(deleted_student.getNume() == 'Berinde')
        self.assertTrue(self.__repo.size() == initial_size + 1)

        student_left = self.__repo.find(676752)
        self.assertEqual(student_left.getNume(), 'Elon')
        self.assertRaises(StudentNotFoundException, self.__repo.delete, 'wrongID')

    def test_edit(self):
        student1 = Student(678825, 'Leo', 6)
        self.__repo.store(student1)
        student2 = Student(676752, 'Elon', 3)
        self.__repo.store(student2)
        student3 = Student(222345, 'Berinde', 15)

        modified_student = self.__repo.edit(678825, student3)
        self.assertEqual(modified_student.getNume(), 'Berinde')
        self.assertEqual(modified_student.getGrup(), 15)
        self.assertRaises(StudentNotFoundException, self.__repo.edit, 6784563, Student(222345, 'Berinde', 15))

    def tearDown(self) -> None:
        self.__repo.delete_all()


if __name__ == '__main__':
    unittest.main()
