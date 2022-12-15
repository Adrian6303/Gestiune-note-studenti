from domain.entities import Student, PbLaborator, Grade
from exceptions.exceptions import *


class InMemoryRepository:
    """
        Clasa creata cu responsabilitatea de a gestiona
        multimea de studenti si probleme (i.e. sa ofere un depozit persistent pentru obiecte
        de tip student si pb)

    """

    def __init__(self):
        # shows - multimea de seriale pe care o gestionam
        # poate fi si dictionar, este la latitudinea noastra cum stocam datele
        # e.g. stocare in dict cu un camp in plus id_serial (dar se poate lua titlu ca si cheie
        # de ex, daca am sti ca e unic):
        # {idSerial1: Serial1, idSerial2: Serial2}
        # vs. [serial1, serial2]
        self.__studenti = []
        self.__probleme = []
        self.__grades = []

    def find_student(self, id):
        """
        Cauta studentul cu id dat
        :param id: id dat
        :type id: int
        :return: studentul cu id dat, None daca nu exista
        :rtype: Student
        """
        for student in self.__studenti:
            if student.getStudentID() == id:
                return student
        return None

    def find_problema(self, nr):
        """
        Cauta problema cu nr dat
        :param nr: nr dat
        :type nr: str
        :return: problema cu nr dat, None daca nu exista
        :rtype: PbLaborator
        """
        for problema in self.__probleme:
            if problema.getNrLab_nrPb() == nr:
                return problema
        return None

    def find_grade(self, g):
        """
        Cauta grade in lista de grades
        :param g: rating-ul cautat
        :type g: grade
        :return: grade-ul cautat daca exista in lista, None altfel
        :rtype: Grade
        """
        for grade in self.__grades:
            if g == grade:
                return grade
        return None

    def store_student(self, student):
        """
        Adauga un student in lista
        :param student: serialul care se adauga
        :type student: Student
        :return: -; lista de studenti se modifica prin adaugarea studentului dat
        :rtype:
        """
        self.__studenti.append(student)

    def store_pbLab(self, problema):
        """
        Adauga un serial in lista
        :param problema: problema care se adauga
        :type problema: PbLaborator
        :return: -; lista de probleme se modifica prin adaugarea problemei date
        :rtype:Nu exista serial cu acest id.
        """
        self.__probleme.append(problema)

    def store_grade(self, grade):
        """
        Adauga un grade
        :param grade: evaluarea de adaugat
        :type grade: Grade
        :return: -; se adauga grade la lista de evaluari
        :rtype: -
        :raises: RatingAlreadyAssignedException daca exista deja rating pentru serialul si clientul dat
        """
        g = self.find_grade(grade)
        if g is not None:
            raise GradeAlreadyAssignedException()
        self.__grades.append(grade)

    def get_all_students(self):
        """
        Returneaza o lista cu toati studenti existenti
        :rtype: list of objects de tip Student
        """
        return self.__studenti

    def get_all_problems(self):
        """
        Returneaza o lista cu toate problemele de laborator existente
        :rtype: list of objects de tip PbLaborator
        """
        return self.__probleme

    def get_all_grades(self):
        """
        Returneaza o lista cu toate evaluarile disponibile
        :return: lista cu evaluarile disponibile
        :rtype: list of Rating objects
        """
        return self.__grades

    def delete_student(self, id):
        """
        Sterge student dupa id
        :param id: id-ul dat
        :type id: int
        :return: studentul sters
        :rtype: Student
        :raises: ValueError daca id-ul nu exista
        """

        student = self.find_student(id)
        if student is None:
            raise ValueError('Nu exista student cu acest id.')

        self.__studenti.remove(student)
        return student

    def delete_pbLab(self, nr):
        """
        Sterge problema dupa nr
        :param nr: nr dat
        :type nr: str
        :return: studentul sters
        :rtype:  PbLaborator
        :raises: ValueError daca nr nu exista
        """

        problema = self.find_problema(nr)
        if problema is None:
            raise ValueError('Nu exista problema cu acest nr.')

        self.__probleme.remove(problema)
        return problema

    def edit_student(self, id, nume, grupa):
        """
                Modifica datele studentului cu id dat
                :param id: id dat
                :type id: int
                :param nume: numele studentului
                :type nume: str
                :param grupa: nr grupei studentului
                :type grupa: int
                :return: studentul-ul modificat
                :rtype: Student
                :raises: ValueError daca id-ul nu exista
                """

        student = self.find_student(id)
        if student is None:
            raise ValueError('Nu exista student cu acest id.')
        else:
            student.setNume(nume)
            student.setGrup(grupa)

        return student

    def edit_pbLab(self, nr, descriere, deadline):
        """
                Modifica datele problemei cu id dat
                :param nr: nr dat
                :type nr: str
                :param descriere: descrierea problemei
                :type descriere: str
                :param deadline: deadline-ul problemei
                :type deadline: str
                :return: problema modificata
                :rtype: PbLaborator
        """
        problem = self.find_problema(nr)
        if problem is None:
            raise ValueError('Nu exista problema cu acest nr.')
        else:
            problem.setDeadline(deadline)
            problem.setDescriere(descriere)

        return problem

    def search_student(self, id):
        """
            Cauta studentul cu id-ul dat
            :param id: id-ul studentului de cautat
            :type id: int
            :return: studentul cautat
            :rtype:Student
            :raises: ValueError daca noile date nu sunt valide, sau nu exista student cu id dat
        """
        student = self.find_student(id)
        if student is None:
            raise ValueError('Nu exista student cu acest id.')
        return student

    def search_pbLab(self, nr):
        """
            Cauta problema cu nr-ul dat
            :param nr: nr-ul problemei de cautat
            :type nr: str
            :return: problema cautata
            :rtype:PbLaborator
            :raises: ValueError daca noile date nu sunt valide, sau nu exista problema cu nr dat
        """
        problema = self.find_problema(nr)
        if problema is None:
            raise ValueError('Nu exista problema cu acest nr.')
        return problema


def setup_test_repo():
    student1 = Student(516728, 'Franz', 1)
    student2 = Student(678192, 'Albert', 12)
    student3 = Student(321312, 'Leonardo', 6)
    student4 = Student(523455, 'Felix', 8)
    student5 = Student(890782, 'Marian', 3)
    student6 = Student(756712, 'Dorel', 6)
    student7 = Student(456189, 'Tiplache', 16)
    student8 = Student(671122, 'Gabi', 4)
    student9 = Student(562824, 'Hans', 9)
    student10 = Student(789012, 'Fernando', 10)

    pbLab1 = PbLaborator('1_2', 'ugahsd', '1 mai')
    pbLab2 = PbLaborator('2_2', 'asdasdsda', '12 martie')
    pbLab3 = PbLaborator('3_5', 'fsdfsdardo', '6 iunie')
    pbLab4 = PbLaborator('6_6', 'adssadasdasx', '8 iulie')
    pbLab5 = PbLaborator('3_7', 'Masdasdasdan', '3 decembrie')
    pbLab6 = PbLaborator('9_3', 'Dasdasddael', '6 ianuarie')
    pbLab7 = PbLaborator('2_10', 'Tsadsadache', '16 mai')
    pbLab8 = PbLaborator('7_2', 'asdsadasdsai', '4 aprilie')
    pbLab9 = PbLaborator('4_6', 'asdasdasdsas', '9 iulie')
    pbLab10 = PbLaborator('1_8', 'asdsdadaando', '10 octombrie')

    test_repo = InMemoryRepository()
    test_repo.store_student(student1)
    test_repo.store_student(student2)
    test_repo.store_student(student3)
    test_repo.store_student(student4)
    test_repo.store_student(student5)
    test_repo.store_student(student6)
    test_repo.store_student(student7)
    test_repo.store_student(student8)
    test_repo.store_student(student9)
    test_repo.store_student(student10)

    test_repo.store_pbLab(pbLab1)
    test_repo.store_pbLab(pbLab2)
    test_repo.store_pbLab(pbLab3)
    test_repo.store_pbLab(pbLab4)
    test_repo.store_pbLab(pbLab5)
    test_repo.store_pbLab(pbLab6)
    test_repo.store_pbLab(pbLab7)
    test_repo.store_pbLab(pbLab8)
    test_repo.store_pbLab(pbLab9)
    test_repo.store_pbLab(pbLab10)

    return test_repo


def test_find():
    test_repo = setup_test_repo()

    s = test_repo.find_student(321312)
    assert (s.getNume() == 'Leonardo')
    assert (s.getGrup() == 6)

    p = test_repo.find_problema('4_6')
    assert (p.getDescriere() == 'asdasdasdsas')
    assert (p.getDeadline() == '9 iulie')

    s1 = test_repo.find_student(567555)
    assert (s1 is None)

    p1 = test_repo.find_problema('12_12')
    assert (p1 is None)


def test_get_all_students():
    test_repo1 = setup_test_repo()
    crt_students = test_repo1.get_all_students()
    assert (type(crt_students) == list)
    assert (len(crt_students) == 10)

    test_repo1.delete_student(890782)
    test_repo1.delete_student(671122)

    crt_students = test_repo1.get_all_students()
    assert (len(crt_students) == 8)

    test_repo1.store_student(Student(577990, 'Mihai', 5))
    crt_students = test_repo1.get_all_students()
    assert (len(crt_students) == 9)

    # not a good test if we don't know if the show is stored on the last position or not
    # e.g. what is returned from get_all_shows for RepoDict?
    assert (test_repo1.get_all_students()[-1].getNume() == 'Mihai')
    assert (test_repo1.get_all_students()[-1].getGrupa() == 5)

    test_repo1.edit_student(577990, 'Raphael', 3)

    # is it always the case that the updated show keeps its position?
    # e.g. implement update as delete(old_show) + insert(new_show)

    assert (test_repo1.get_all_students()[-1].getGrupa() == 3)
    assert (test_repo1.get_all_students()[-1].getNume() == 'Raphael')
    crt_students = test_repo1.get_all_students()
    assert (len(crt_students) == 9)


def test_get_all_pbLab():
    test_repo1 = setup_test_repo()
    crt_problems = test_repo1.get_all_problems()
    assert (type(crt_problems) == list)
    assert (len(crt_problems) == 10)

    test_repo1.delete_pbLab('3_7')
    test_repo1.delete_pbLab('9_3')

    crt_problems = test_repo1.get_all_problems()
    assert (len(crt_problems) == 8)

    test_repo1.store_pbLab(PbLaborator('9_11', 'dgsyuadsa', '5 aprilie'))
    crt_problems = test_repo1.get_all_problems()
    assert (len(crt_problems) == 9)

    # not a good test if we don't know if the show is stored on the last position or not
    # e.g. what is returned from get_all_shows for RepoDict?
    assert (test_repo1.get_all_problems()[-1].getDescriere() == 'dgsyuadsa')
    assert (test_repo1.get_all_problems()[-1].getDeadline() == '5 aprilie')

    test_repo1.edit_pbLab('9_11', 'guguasdgsa', '6 aprilie')

    # is it always the case that the updated show keeps its position?
    # e.g. implement update as delete(old_show) + insert(new_show)

    assert (test_repo1.get_all_problems()[-1].getDescriere() == 'guguasdgsa')
    assert (test_repo1.get_all_students()[-1].getDeadline() == '6 aprilie')
    crt_problems = test_repo1.get_all_problems()
    assert (len(crt_problems) == 9)


def test_store_student():
    test_repo = InMemoryRepository()
    student1 = Student(617821, 'Mircea', 3)
    test_repo.store_student(student1)

    crt_students = test_repo.get_all_students()
    assert (len(crt_students) == 1)
    student2 = Student(121333, 'Max', 5)
    test_repo.store_student(student2)
    crt_students = test_repo.get_all_students()
    assert (len(crt_students) == 2)

    try:
        # duplicate id
        test_repo.store_student(student2)
        assert False
    except ValueError:
        assert True


def test_store_problem():
    test_repo = InMemoryRepository()
    problem1 = PbLaborator("1_3", 'asdasad', '3 mai')
    test_repo.store_pbLab(problem1)

    crt_problems = test_repo.get_all_problems()
    assert (len(crt_problems) == 1)
    problem2 = PbLaborator('2_5', 'asadasd', '4 mai')
    test_repo.store_pbLab(problem2)
    crt_problems = test_repo.get_all_problems()
    assert (len(crt_problems) == 2)

    try:
        # duplicate id
        test_repo.store_pbLab(problem2)
        assert False
    except ValueError:
        assert True
