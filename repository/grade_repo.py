from domain.entities import Student, PbLaborator, Grade
from exceptions.exceptions import *

class GradeFileRepo:
    def __init__(self, filename):
        self.__filename = filename

    def __load_from_file(self):
        """
        Incarca datele din fisier
        :return: lista de studenti din fisier
        :rtype: list of Student objects
        :raises: ...
        """
        try:
            f = open(self.__filename, 'r')
            # f = io.open(self.__filename, mode='r', encoding='utf-8')
        except IOError:
            return

        lines = f.readlines()
        # lines: ['C1001;Superstore;2019;98', 'F1001; Arrow;2012;170',...]
        all_grades = []
        for line in lines:
            grade_stud, grade_pbLab, grade_val = [token.strip() for token in line.split(';')]
            grade_val = float(grade_val)
            grade_stud = int(grade_stud)

            g = Grade(grade_stud, grade_pbLab, grade_val)
            all_grades.append(g)

        f.close()
        return all_grades

    def __save_to_file(self, all_grades):
        """
        Salveaza studenti in fisier
        """
        with open(self.__filename, 'w') as f:
            for grade in all_grades:

                grade_string = str(grade.getStudent()) + ';' + str(grade.getPbLab()) + ';' + str(
                    grade.getGrade()) + '\n'
                f.write(grade_string)

    def find(self, g):
        """
        Cauta studentul cu id dat
        :param id: id dat
        :type id: str
        :return: student cu id dat, None daca nu exista serial cu id dat
        :rtype: Student
        """
        all_grades = self.__load_from_file()

        for grade in all_grades:
            if g == grade:
                return grade
        return None

    def store(self, grade):
        """
       Adauga un serial in lista
       :param student: studentul care se adauga
       :type student: Student
       :return: -; lista de studenti se modifica prin adaugarea studentului dat
        :rtype:
        :raises: DuplicateIDException daca studentul exista deja
        """
        all_grades = self.__load_from_file()

        g = self.find(grade)
        if g is not None:
            raise GradeAlreadyAssignedException()
        all_grades.append(grade)
        self.__save_to_file(all_grades)

    def get_all(self):
        """
        Returneaza o lista cu toati studenti
        :rtype: list of objects de tip Student
        """
        return self.__load_from_file()

    def size(self):
        """
        Returneaza numarul de studenti din multime
        :return: numar seriale existente
        :rtype:int
        """
        return len(self.__load_from_file())

    def __find_index(self, all_grades, grade):
        """
        Gaseste pozitia in lista a studentul cu id dat
        :param all_students: lista cu toati studenti
        :type all_students: list of Students objects
        :param id: id-ul cautat
        :type id: str
        :return: pozitia in lista a studentilor dat, -1 daca studentul nu se regaseste in lista
        :rtype: int, >=0, <repo.size()
        """
        index = -1
        for i in range(len(all_grades)):
            if all_grades[i] == grade:
                index = i

        return index

    def delete_all(self):
        self.__save_to_file([])