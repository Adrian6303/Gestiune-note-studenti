import unittest

from domain.entities import PbLaborator
from domain.validators import Validator
from exceptions.exceptions import ValidationException


class TestCasePbLaboratorDomain(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = Validator()

    def test_create_pbLab(self):
        pbLab1 = PbLaborator('2_7', 'Cautare numere prime', '4 martie')
        self.assertEqual(pbLab1.getNrLab_nrPb(), '2_7')
        self.assertEqual(pbLab1.getDescriere(), 'Cautare numere prime')
        self.assertEqual(pbLab1.getDeadline(), '4 martie')

        pbLab1.setNrLab_nrPb('5_12')
        pbLab1.setDescriere('Divizorii comuni')
        pbLab1.setDeadline('7 iunie')

        self.assertEqual(pbLab1.getNrLab_nrPb(), '5_12')
        self.assertEqual(pbLab1.getDescriere(), 'Divizorii comuni')
        self.assertEqual(pbLab1.getDeadline(), '7 iunie')

    def test_equals_pbLab(self):
        pbLab1 = PbLaborator('2_7', 'Cautare numere prime', '5 martie')
        pbLab2 = PbLaborator('2_7', 'Cautare numere prime', '5 martie')

        self.assertEqual(pbLab1, pbLab2)

        pbLab3 = PbLaborator('2_10', 'Cautare numere prime', '10 martie')
        self.assertNotEqual(pbLab1, pbLab3)

    def test_pbLab_validator(self):
        pbLab1 = PbLaborator('2_7', 'Cautare numere prime', '4 martie')
        self.__validator.validate_pbLab(pbLab1)
        pbLab2 = PbLaborator('2_7', '', '4 martie')
        pbLab3 = PbLaborator('2', 'Cautare numere prime', '4 martie')

        self.assertRaises(ValidationException, self.__validator.validate_pbLab, pbLab2)
        self.assertRaises(ValidationException, self.__validator.validate_pbLab, pbLab3)


if __name__ == '__main__':
    unittest.main()
