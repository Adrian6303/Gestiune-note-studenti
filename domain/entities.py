class Student:
    no_instances = 0

    def __init__(self, studentID, nume, grup):
        """
        Creeaza un nou student
        :param studentID: id student
        :type studentID: int
        :param nume: nume student
        :type nume: str
        :param grup: numarul grupei
        :type grup: int (>0)
        """
        self.__lista_stud = {'studentID': None, 'nume': None, 'grup': None}

        self.__lista_stud['studentID'] = studentID
        self.__lista_stud['nume'] = nume
        self.__lista_stud['grup'] = grup

        Student.no_instances += 1

    def getStudentID(self):
        return self.__lista_stud['studentID']

    def getNume(self):
        return self.__lista_stud['nume']

    def getGrup(self):
        return self.__lista_stud['grup']

    def setStudentID(self, value):
        self.__lista_stud['studentID'] = value

    def setNume(self, value):
        self.__lista_stud['nume'] = value

    def setGrup(self, value):
        self.__lista_stud['grup'] = value

    def __eq__(self, other):
        """
        Verifica egalitatea intre studentul curent si studentul other
        :param other:
        :type other: Student
        :return: True daca studentii sunt egali (=au IDstudent identic), False altfel
        :rtype: bool
        """
        if self.__lista_stud['studentID'] == other:
            return True
        return False

    def __str__(self):
        return "ID Student: " + str(self.__lista_stud['studentID']) + '; Nume: ' + str(
            self.__lista_stud['nume']) + '; Grupa: ' + str(self.__lista_stud['grup'])

    @staticmethod
    def getNumberOfStudentObjects():
        return Student.no_instances


def test_create_student():
    student1 = Student(578102, 'Marinache Iberiu', 4)
    assert (student1.getStudentID() == 578102)
    assert (student1.getNume() == 'Marinache Iberiu')
    assert (student1.getGrup() == 4)

    student1.setStudentID(567123)
    student1.setNume('Pasare Valeriu')
    student1.setGrup(7)

    assert (student1.getStudentID() == 567123)
    assert (student1.getNume() == 'Pasare Valeriu')
    assert (student1.getGrup() == 7)


def test_equals_student():
    student1 = Student(895176, 'Randunica Adriana', 12)
    student2 = Student(895176, 'Randunica Adriana', 10)

    assert (student1 == student2)

    student3 = Student(128626, 'Randunica Adriana', 12)
    assert (student1 != student3)


test_create_student()
test_equals_student()


class PbLaborator:
    no_instances = 0
    """
    Creeaza o noua problema de laborator: 
    :param nrLab_nrPb: nr laborator si nr problema
    :type nrLab_nrPb: str
    :param descriere: descriere problema
    :type descriere: str
    :param deadline: deta limita
    :type deadline: str
    """

    def __init__(self, nrLab_nrPb, descriere, deadline):
        self.__lista_lab = {'nr': None, 'descriere': None, 'deadLine': None}

        self.__lista_lab['nr'] = nrLab_nrPb
        self.__lista_lab['descriere'] = descriere
        self.__lista_lab['deadLine'] = deadline

        PbLaborator.no_instances += 1

    def getNrLab_nrPb(self):
        return self.__lista_lab['nr']

    def getDescriere(self):
        return self.__lista_lab['descriere']

    def getDeadline(self):
        return self.__lista_lab['deadLine']

    def setNrLab_nrPb(self, value):
        self.__lista_lab['nr'] = value

    def setDescriere(self, value):
        self.__lista_lab['descriere'] = value

    def setDeadline(self, value):
        self.__lista_lab['deadLine'] = value

    def __eq__(self, other):
        """
        Verifica egalitatea intre problema curent si problema other
        :param other:
        :type other: PbLaborator
        :return: True daca problemele sunt egale (=au acelasi numar), False altfel
        :rtype: bool
        """
        if self.__lista_lab['nr'] == other.getNrLab_nrPb():
            return True
        return False

    def __str__(self):
        return "Nr lab si nr problema: " + str(self.__lista_lab['nr']) + '; Descriere: ' + str(
            self.__lista_lab['descriere']) + '; Deadline: ' + str(
            self.__lista_lab['deadLine'])

    @staticmethod
    def getNumberOfProblemObjects():
        return PbLaborator.no_instances


def test_create_PbLaborator():
    PbLaborator1 = PbLaborator('2_7', 'Cautare numere prime', '4 martie')
    assert (PbLaborator1.getNrLab_nrPb() == '2_7')
    assert (PbLaborator1.getDescriere() == 'Cautare numere prime')
    assert (PbLaborator1.getDeadline() == '4 martie')

    PbLaborator1.setNrLab_nrPb('5_12')
    PbLaborator1.setDescriere('Divizorii comuni')
    PbLaborator1.setDeadline('7 iunie')

    assert (PbLaborator1.getNrLab_nrPb() == '5_12')
    assert (PbLaborator1.getDescriere() == 'Divizorii comuni')
    assert (PbLaborator1.getDeadline() == '7 iunie')


def test_equals_PbLaborator():
    PbLaborator1 = PbLaborator('2_7', 'Cautare numere prime', '5 martie')
    PbLaborator2 = PbLaborator('2_7', 'Cautare numere prime', '1 martie')

    assert (PbLaborator1 == PbLaborator2)

    PbLaborator3 = PbLaborator('2_10', 'Cautare numere prime', '10 martie')
    assert (PbLaborator1 != PbLaborator3)


class Grade:
    def __init__(self, student, pbLab, grade):
        self.__student = student
        self.__pbLab = pbLab
        self.__grade = grade

    def getStudent(self):
        return self.__student

    def getPbLab(self):
        return self.__pbLab

    def getGrade(self):
        return self.__grade

    def setStudent(self, value):
        self.__student = value

    def setPbLab(self, value):
        self.__pbLab = value

    def setGrade(self, value):
        self.__grade = value

    def __eq__(self, other):
        if self.__student == other.__student and self.__pbLab == other.__pbLab:
            return True
        return False

    def __str__(self):
        return 'Studentul: [ID:' + str(self.__student) + ']' + \
               'PbLab: [' + str(self.__pbLab) + '],' + 'Grade: ' + str(self.__grade)


test_create_student()
test_equals_student()

test_create_PbLaborator()
test_equals_PbLaborator()
