import unittest

from domain.validators import Validator
from exceptions.exceptions import ValidationException, PbLabNotFoundException
from repository.pbLab_repo import PbLabFileRepo
from service.pbLab_service import PbLabService


class TestCasePbLabService(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = PbLabFileRepo('test_e_pbLab_service.txt')
        validator = Validator()
        self.__srv = PbLabService(self.__repo, validator)

    def test_add_pbLab(self):

        added_student = self.__srv.add_pbLab('2_77', 'ceva nou', '5 februarie')
        self.assertTrue(added_student.getDescriere() == 'ceva nou')
        self.assertTrue(added_student.getDeadline() == '5 februarie')

        self.assertEqual(len(self.__srv.get_all_problems()), 1)
        self.assertRaises(ValidationException, self.__srv.add_pbLab, '2_789', 'ceva', '5 februarie')

    def test_delete_pbLab(self):

        self.__srv.add_pbLab('2_77', 'ceva nou', '5 februarie')
        deleted_student = self.__srv.delete_pbLab('2_77')

        self.assertEqual(len(self.__srv.get_all_problems()), 0)
        self.assertEqual(deleted_student.getDescriere(), 'ceva nou')
        self.assertEqual(deleted_student.getDeadline(), '5 februarie')
        self.assertRaises(PbLabNotFoundException, self.__srv.delete_pbLab, '3_2')

    def test_get_all_pbLab(self):

        self.__srv.add_pbLab('2_77', 'ceva nou', '5 februarie')
        self.__srv.add_pbLab('5_7', 'ceva', '7 februarie')
        self.assertIsInstance(self.__srv.get_all_problems(), list)
        self.assertEqual(len(self.__srv.get_all_problems()), 2)

    def test_edit_pbLab(self):

        self.__srv.add_pbLab('2_77', 'ceva nou', '5 februarie')
        updated_pbLab = self.__srv.edit_pbLab('2_77', 'altceva', '7 mai')

        self.assertTrue(updated_pbLab.getDescriere() == 'altceva')
        self.assertTrue(updated_pbLab.getDeadline() == '7 mai')
        self.assertRaises(PbLabNotFoundException,self.__srv.edit_pbLab, '7_7',  'ceva nou', '5 februarie')

    def tearDown(self) -> None:
        self.__repo.delete_all()
