from domain.entities import Student
from domain.validators import Validator
from repository.student_repo import StudentFileRepo
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
        self.__repo.store(s)
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
        return self.__repo.delete(id)

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
        return self.__repo.edit(id, s)

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
        return self.__repo.find(id)
