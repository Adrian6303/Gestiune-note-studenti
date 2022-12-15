from domain.entities import Student, PbLaborator, Grade
from domain.dtos import PbLabStudentGrade
from domain.validators import Validator
from repository.in_memo_repo import InMemoryRepository
from exceptions.exceptions import *


class StudentService:
    def __init__(self, repo, validator):
        """
        Initializeaza service
        :param repo: obiect de tip repo care ne ajuta sa gestionam multimea de seriale
        :type repo: InMemoryRepository
        :param validator: validator pentru verificarea serialelor
        :type validator: ShowValidator
        """
        self.__repo = repo
        self.__validator = validator

    def add_student(self, studentID, nume, grupa):
        """
        Adauga student
        :param studentID: Id-ul studentului
        :type studentID:int
        :param nume: numele studentului
        :type nume:str
        :param grupa:numarul grupei de care apartine
        :type grupa:int
        :return: obiectul de tip Student creat
        :rtype:-; studentul s-a adaugat in lista
        :raises: ValueError daca studentul are date invalide
        """
        s = Student(studentID, nume, grupa)

        self.__validator.validate_student(s)
        self.__repo.store_student(s)
        return s

    def get_all_students(self):
        """
        Returneaza o lista cu toati studenti disponibili
        :return: lista de studenti disponibili
        :rtype: list of objects de tip Student
        """
        return self.__repo.get_all()

    def delete_student(self, id):
        """
        Sterge serialul cu id dat din lista
        :param id: id-ul dat
        :type id: int
        :return: studentul sters
        :rtype: Serial
        :raises: ValueError daca nu exista serial cu id-ul dat
        """
        self.__validator.validate_StudentID(id)
        return self.__repo.delete_student(id)

    def edit_student(self, id, nume, grupa):
        """
                Modifica datele studentului cu id dat
                :param id: id-ul serialului de modificat
                :type id: int
                :param nume: noul titlu al serialului
                :type nume: str
                :param grupa: noul an de aparitie al serialului
                :type grupa: int
                :return: studentul modificat
                :rtype:Student
                :raises: ValueError daca noile date nu sunt valide, sau nu exista student cu id dat
                """
        s = Student(id, nume, grupa)

        self.__validator.validate_student(s)
        return self.__repo.edit_student(id, nume, grupa)

    def search_student(self, id):
        """
            Cauta studentul cu id-ul dat
            :param id: id-ul studentului cautat
            :type id: int
            :return: studentul cautat
            :rtype:Student
            :raises: ValueError daca noile date nu sunt valide, sau nu exista student cu id dat
        """
        self.__validator.validate_StudentID(id)
        return self.__repo.search_student(id)


class LabService:
    """
        GRASP Controller (Curs 6)
        Responsabil de efectuarea operatiilor cerute de utilizator
        Coordoneaza operatiile necesare pentru a realiza actiunea declansata de utilizator
        (i.e. declansare actiune: utilizator -> ui-> obiect tip service in ui -> service -> service coordoneaza operatiile
        folosind alte obiecte (e.g. repo, validator) pentru a realiza efectiv operatia)
        """

    def __init__(self, repo, validator):
        """
        Initializeaza service
        :param repo: obiect de tip repo care ne ajuta sa gestionam multimea de seriale
        :type repo: InMemoryRepository
        :param validator: validator pentru verificarea serialelor
        :type validator: ShowValidator
        """
        self.__repo = repo
        self.__validator = validator

    def add_pbLab(self, nrLab_nrPb, descriere, deadline):
        """
        Adauga pbLab
        :param nrLab_nrPb: nr lab si nr pb
        :type nrLab_nrPb:str
        :param descriere: descrierea problemei
        :type descriere:str
        :param deadline:termenul de predare a problemei
        :type deadline:str
        :return: obiectul de tip PbLaborator creat
        :rtype:-; problema s-a adaugat in lista
        :raises: ValueError daca problema are date invalide
        """
        p = PbLaborator(nrLab_nrPb, descriere, deadline)

        self.__validator.validate_pbLab(p)
        self.__repo.store_pbLab(p)
        return p

    def get_all_problems(self):
        """
        Returneaza o lista cu toate problemele disponibile
        :return: lista de probleme disponibile
        :rtype: list of objects de tip PbLaborator
        """
        return self.__repo.get_all_problems()

    def delete_pbLab(self, nr):
        """
        Sterge serialul cu id dat din lista
        :param nr: numarul dat
        :type nr: str
        :return: problema stearsa
        :rtype: PbLaborator
        :raises: ValueError daca nu exista problema cu nr dat
        """
        self.__validator.validate_NrLab_nrPb(nr)
        return self.__repo.delete_pbLab(nr)

    def edit_pbLab(self, nr, descriere, deadline):
        """
                        Modifica datele problemei cu id dat
                        :param nr: nr problemei de modificat
                        :type nr: str
                        :param descriere: noua descriere a problemei
                        :type descriere: str
                        :param deadline: noul termen limita a problemei
                        :type deadline: int
                        :return: problema modificata
                        :rtype:PbLaborator
                        :raises: ValueError daca noile date nu sunt valide, sau nu exista problema cu nr dat
                        """
        pb = PbLaborator(nr, descriere, deadline)

        self.__validator.validate_pbLab(pb)
        return self.__repo.edit_pbLab(nr, descriere, deadline)

    def search_pbLab(self, nr):
        """
            Cauta problema cu nr-ul dat
            :param nr: nr-ul problemei
            :type nr: str
            :return: problema cautata
            :rtype: PbLaborator
            :raises: ValueError daca noile date nu sunt valide, sau nu exista problema cu nr dat
        """
        self.__validator.validate_NrLab_nrPb(nr)
        return self.__repo.search_pbLab(nr)


class GradeService:
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator


    def create_grade(self, student_id, pbLab_nr, grade_val):
        """
        Creeaza un grade
        :param student_id: id-ul studentului-ului evaluat
        :type student_id: int
        :param pbLab_nr: id-ul problemei
        :type pbLab_nr: str
        :param grade_val: nota acordata studentului (1-10)
        :type grade_val: float
        :return: rating-ul creat cu datele date
        :rtype: Rating
        :raises: ShowNotFoundException
                 ClientNotFoundException
                 ValidationException
                 RatingAlreadyAssignedException
        """
        student = self.__repo.find_student(student_id)
        if student is None:
            raise StudentNotFoundException()

        pb_lab = self.__repo.find_problema(pbLab_nr)

        if pb_lab is None:
            raise PbLabNotFoundException()

        grade = Grade(student, pb_lab, grade_val)
        self.__validator.validate_grade(grade)
        self.__repo.store_grade(grade)
        return grade

    def get_all_grades(self):
        return self.__repo.get_all_grades()

    def get_avg_sub5(self):
        all_grades = self.__repo.get_all_grades()
        all_students= self.__repo.get_all_students()
        ok=False
        for stud in all_students:
            media = 0
            nr = 0
            for grade in all_grades:

                if grade.getStudent().getStudentID() == stud.getStudentID():
                    media+=int(grade.getGrade())
                    nr+=1
            if nr>0:
                media=float(media/nr)
                if media < 5:
                    print("Studentul: "+ str(stud.getNume()) + "(ID: " + str(stud.getStudentID()) +"), media:" + str(media))
                    ok=True
        return ok

    def stat_studenti_note(self, nr):
        all_grades = self.__repo.get_all_grades()
        studenti=[]
        ok=False
        for grade in all_grades:
            if grade.getPbLab().getNrLab_nrPb() == nr:
                studenti.append(grade.getStudent().getNume())

        if len(studenti)>0:
            ok=True
            studenti = sorted(studenti)
            for stud in studenti:
                for grade in all_grades:
                    if stud == grade.getStudent().getNume() and grade.getPbLab().getNrLab_nrPb() == nr:
                        print('Studentul:' + str(stud) + 'cu nota: ' + str(grade.getGrade()))

        return ok

    def get_media_max(self):
        all_grades = self.__repo.get_all_grades()
        all_students = self.__repo.get_all_students()
        ok = False
        max_medie=0

        for stud in all_students:
            media = 0
            nr = 0
            for grade in all_grades:

                if grade.getStudent().getStudentID() == stud.getStudentID():
                    media+=int(grade.getGrade())
                    nr+=1
            if nr>0:
                media=float(media/nr)
                if max_medie < media:
                    max_medie = float(media)
                    student = stud.getNume()
                    ok = True

        if ok==True:
            print('Studentul:' + str(student) + 'cu media: ' + str(max_medie))

        return ok
    # def get_top_shows(self, pbLab_nr, n=3):
    #     """
    #     Returneaza primele 3 show-uri cu cele mai bune rating-uri pentru un client dat
    #     :param client_id: id-ul clientului
    #     :type client_id: str
    #     :param n: numarul de seriale de afisat (default 3)
    #     :type n: int
    #     :return: lista cu obiecte DTO ClientShow
    #     :rtype: list of ClientShow objects
    #     """
    #     client = self.__pbLab_repo.find(pbLab_nr)
    #
    #     if client is None:
    #         raise ClientNotFoundException()
    #
    #     all_ratings = self.__rating_repo.get_all()
    #     client_ratings = []
    #
    #     for rating in all_ratings:
    #         if rating.getClient().getId() == client_id:
    #             client_show_r = ClientShowRating(rating.getClient().getNume(), rating.getSerial().getTitle(),
    #                                              rating.getNoStars())
    #             client_ratings.append(client_show_r)
    #
    #     # handle the case when we don't have enough ratings - either proceed
    #     # and return what we have
    #     # or throw an exception
    #     client_ratings = sorted(client_ratings, key=lambda x: x.getNoStars(), reverse=True)
    #     client_ratings = client_ratings[:n]
    #
    #     return client_ratings
    #
    #


def test_add_student():
    repo = InMemoryRepository()
    validator = Validator()
    test_srv = StudentService(repo, validator)

    added_student = test_srv.add_student(545677, 'Tractoreanu Leonardo', 12)
    assert (added_student.getStudentID() == 545677)
    assert (added_student.getNume() == 'Tractoreanu Leonardo')
    assert (added_student.getGrup() == 12)

    assert (len(test_srv.get_all_students()) == 1)

    try:
        added_student = test_srv.add_student(545, 'Tractoreanu Leonardo', 12)
        assert False
    except ValueError:
        assert True


def test_add_probleme():
    repo = InMemoryRepository()
    validator = Validator()
    test_srv = LabService(repo, validator)

    added_problem = test_srv.add_pbLab('1_5', 'Sirul lui Fibbonaci', '10 octombrie')
    assert (added_problem.getNrLab_nrPb() == '1_5')
    assert (added_problem.getDescriere() == 'Sirul lui Fibbonaci')
    assert (added_problem.getDeadline() == '10 octombrie')

    assert (len(test_srv.get_all_problems()) == 1)

    try:
        added_problem = test_srv.add_pbLab('1231233_51231', 'Sirul lui Fibbonaci', '10 octombrie')
        assert False
    except ValueError:
        assert True
