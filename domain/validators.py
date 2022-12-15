from domain.entities import Student, PbLaborator, Grade
from exceptions.exceptions import *


class Validator:
    def validate_student(self, student):
        errors = []
        if student.getStudentID() < 100000 or student.getStudentID() >= 1000000:
            errors.append('Id-ul studentului trebuie sa aiba mai mult de 6 cifre.')
        if len(student.getNume()) < 3:
            errors.append('Numele trebuie sa aiba cel putin 3 litere.')
        if student.getGrup() < 1 or student.getGrup() > 99:
            errors.append('Numarul grupei trebuie sa fie intre 1-99.')

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValidationException(errors_string)

    def validate_pbLab(self, pbLab):
        errors = []
        nr = pbLab.getNrLab_nrPb()
        try:
            l = nr.split('_')
            if int(l[0]) < 1 or int(l[0]) > 20:
                errors.append('Nr laboratorului nu este din intervalul [1,20].')
            if int(l[1]) < 1 or int(l[1]) > 100:
                errors.append('Nr problemei nu este din intervalul [1,100].')
        except IndexError:
            errors.append('Numarul problemei nu este de forma corecta.')

        if len(pbLab.getDescriere()) < 3:
            errors.append('Descrierea trebuie sa aiba cel putin 5 litere.')
        if len(pbLab.getDeadline()) < 5 or len(pbLab.getDeadline()) > 15:
            errors.append('Data invalida.')

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValidationException(errors_string)
    def validate_grade(self, grade):
        errors = []
        if grade.getGrade() < 0 or grade.getGrade() > 10:
            errors.append('Nota poate fi intre 1 si 10.')

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValidationException(errors_string)
    def validate_StudentID(self, id):
        errors = []
        if id < 100000 or id >= 1000000:
            errors.append('Id-ul studentului trebuie sa aiba mai mult de 6 cifre.')
        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)

    def validate_NrLab_nrPb(self, nr):
        errors = []
        try:
            l = nr.split('_')
            if int(l[0]) < 1 or int(l[0]) > 20:
                errors.append('Nr laboratorului nu este din intervalul [1,20].')
            if int(l[1]) < 1 or int(l[1]) > 100:
                errors.append('Nr problemei nu este din intervalul [1,100].')
            if len(errors) > 0:
                errors_string = '\n'.join(errors)
                raise ValueError(errors_string)
        except IndexError:
            errors.append('Numarul nu este de forma corecta.')
            errors_string = '\n'.join(errors)
            raise ValidationException(errors_string)


def test_student_validator():
    test_validator = Validator()
    student1 = Student(545677, 'Tractoreanu Leonardo', 12)
    test_validator.validate_student(student1)
    student2 = Student(5712, '', 55)

    try:
        test_validator.validate_student(student2)
        assert False
    except ValueError:
        assert True

    student3 = Student(680456, 'Vancea Alexandru', -55)
    try:
        test_validator.validate_student(student3)
        assert False
    except ValueError:
        assert True


def test_pbLab_validator():
    test_validator = Validator()
    pbLab1 = PbLaborator('1_5', 'Sirul lui Fibbonaci', '2 octombrie')
    test_validator.validate_pbLab(pbLab1)
    pbLab2 = PbLaborator('1_5', '', '2 octombrie')

    try:
        test_validator.validate_pbLab(pbLab2)
        assert False
    except ValueError:
        assert True

    pbLab3 = PbLaborator('-11_5', 'Sirul lui Fibbonaci', '2 octombrie')
    try:
        test_validator.validate_pbLab(pbLab3)
        assert False
    except ValueError:
        assert True
