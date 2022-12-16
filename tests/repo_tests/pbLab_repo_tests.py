import unittest

from domain.entities import PbLaborator
from exceptions.exceptions import DuplicateNrException, PbLabNotFoundException
from repository.pbLab_repo import PbLabFileRepo


class TestCasePbLabRepoFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = PbLabFileRepo('test_pbLab_repo.txt')
        self.__repo.delete_all()
        self.__populate_list()

    def __populate_list(self):
        pbLab1 = PbLaborator('2_77', 'ceva nou', '5 februarie')
        pbLab2 = PbLaborator('4_89', 'vywgorcnehokcbdygwr', '24 martie')
        pbLab3 = PbLaborator('5_6', 'ceva', '1 mai')
        pbLab4 = PbLaborator('3_9', 'asui', '3 aprilie')
        pbLab5 = PbLaborator('7_4', 'guusishaa', '3 mai')
        pbLab6 = PbLaborator('9_9', 'uishdis', '10 iulie')
        pbLab7 = PbLaborator('8_1', 'ajdabsa', '2 iunie')
        pbLab8 = PbLaborator('3-11', 'gyusdadasb', '3 iunie')
        pbLab9 = PbLaborator('4_6', 'hsaisdjsakkas', '5 decembrie')
        pbLab10 = PbLaborator('5_16', 'hihkas', '1 aprilie')

        self.__repo.store(pbLab1)
        self.__repo.store(pbLab2)
        self.__repo.store(pbLab3)
        self.__repo.store(pbLab4)
        self.__repo.store(pbLab5)
        self.__repo.store(pbLab6)
        self.__repo.store(pbLab7)
        self.__repo.store(pbLab8)
        self.__repo.store(pbLab9)
        self.__repo.store(pbLab10)

    def test_find(self):
        p = self.__repo.find('4_6')
        self.assertTrue(p.getNrLab_nrPb() == '4_6')
        self.assertTrue(p.getDescriere() == 'hsaisdjsakkas')
        self.assertEqual(p.getDeadline(), '5 decembrie')

        p1 = self.__repo.find('3_7')
        self.assertIs(p1, None)

    def test_size(self):
        initial_size = self.__repo.size()
        self.__repo.delete('4_6')
        self.__repo.delete('5_16')

        self.assertEqual(self.__repo.size(), initial_size - 2)

        self.__repo.store(PbLaborator('8_8', 'dhiausa', '3 aprilie'))
        self.assertEqual(self.__repo.size(), initial_size - 1)
        self.__repo.edit('8_8', PbLaborator('8_8', 'dhiausa', '8 aprilie'))
        self.assertEqual(self.__repo.size(), initial_size - 1)

    def test_get_all(self):
        initial_size = self.__repo.size()
        crt_pbLab = self.__repo.get_all()
        self.assertIsInstance(crt_pbLab, list)

        self.assertEqual(len(crt_pbLab), initial_size)

        self.__repo.delete('8_1')
        self.__repo.delete('3-11')

        crt_pbLab = self.__repo.get_all()
        self.assertEqual(len(crt_pbLab), initial_size - 2)

        self.__repo.store(PbLaborator('5_21', 'agusa', '1 mai'))
        self.assertTrue(self.__repo.size() == initial_size - 1)

        self.__repo.edit('5_21', PbLaborator('5_21', 'agusaas', '3 mai'))

        self.assertTrue(self.__repo.size() == initial_size - 1)

    def test_store(self):
        initial_size = self.__repo.size()
        pbLab1 = PbLaborator('5_22', 'agudasdadssaas', '3 mai')
        self.__repo.store(pbLab1)

        self.assertEqual(self.__repo.size(), initial_size + 1)
        pbLab2 = PbLaborator('6_21', 'agusaaaas', '8 mai')
        self.__repo.store(pbLab2)
        self.assertEqual(self.__repo.size(), initial_size + 2)
        self.assertRaises(DuplicateNrException, self.__repo.store, pbLab2)

    def test_delete(self):
        initial_size = self.__repo.size()
        pbLab1 = PbLaborator('7_21', 'ioslak', '10 mai')
        self.__repo.store(pbLab1)
        pbLab2 = PbLaborator('5_11', 'asdajoila', '1 mai')
        self.__repo.store(pbLab2)

        deleted_pbLab = self.__repo.delete('7_21')
        self.assertTrue(deleted_pbLab.getDescriere() == 'ioslak')
        self.assertTrue(self.__repo.size() == initial_size + 1)

        pbLab_left = self.__repo.find('5_11')
        self.assertEqual(pbLab_left.getDescriere(), 'asdajoila')
        self.assertRaises(PbLabNotFoundException, self.__repo.delete, 'wrongID')

    def test_edit(self):
        pbLab1 = PbLaborator('15_11', 'asdajoila', '7 mai')
        self.__repo.store(pbLab1)
        pbLab2 = PbLaborator('9_12', 'asdadas', '2 mai')
        self.__repo.store(pbLab2)
        pbLab3 = PbLaborator('9_1', 'asd', '7 mai')

        modified_pbLab = self.__repo.edit('15_11', pbLab3)
        self.assertEqual(modified_pbLab.getDescriere(), 'asd')
        self.assertEqual(modified_pbLab.getDeadline(), '7 mai')
        self.assertRaises(PbLabNotFoundException, self.__repo.edit, '22_22', PbLaborator('9_1', 'asd', '7 mai'))

    def tearDown(self) -> None:
        self.__repo.delete_all()


if __name__ == '__main__':
    unittest.main()
