from domain.entities import PbLaborator
from exceptions.exceptions import *




class PbLabFileRepo:
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
        all_problems = []
        for line in lines:
            problema_nr, problema_descriere, problema_deadline = [token.strip() for token in line.split(';')]

            p = PbLaborator(problema_nr, problema_descriere, problema_deadline)
            all_problems.append(p)

        f.close()
        return all_problems

    def __save_to_file(self, all_problems):
        """
        Salveaza studenti in fisier
        """
        with open(self.__filename, 'w') as f:
            for problem in all_problems:
                problem_string = str(problem.getNrLab_nrPb()) + ';' + str(problem.getDescriere()) + ';' + str(
                    problem.getDeadline()) + '\n'
                f.write(problem_string)

    def find(self, nr):
        """
        Cauta studentul cu id dat
        :param id: id dat
        :type id: str
        :return: student cu id dat, None daca nu exista serial cu id dat
        :rtype: Student
        """
        all_problems = self.__load_from_file()
        for problem in all_problems:
            if problem.getNrLab_nrPb() == nr:
                return problem
        return None

    def store(self, problem):
        """
       Adauga un serial in lista
       :param problem: studentul care se adauga
       :type problem: Student
       :return: -; lista de studenti se modifica prin adaugarea studentului dat
        :rtype:
        :raises: DuplicateIDException daca studentul exista deja
        """
        all_problems = self.__load_from_file()
        if problem in all_problems:
            raise DuplicateNrException()

        all_problems.append(problem)
        self.__save_to_file(all_problems)

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

    def __find_index(self, all_problems, nr):
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
        for i in range(len(all_problems)):
            if all_problems[i].getNrLab_nrPb() == nr:
                index = i

        return index

    def delete(self, nr):
        """
        Sterge student dupa id
        :param nr: id-ul dat
        :type nr: str
        :return: studentul sters
        :rtype: Student
        :raises: StudentNotFoundException daca id-ul nu exista
        """
        all_problems = self.__load_from_file()
        index = self.__find_index(all_problems, nr)
        if index == -1:
            raise StudentNotFoundException()

        deleted_problem = all_problems.pop(index)

        self.__save_to_file(all_problems)
        return deleted_problem

    def edit(self, nr, modified_problem):
        """
        Modifica datele serialului cu id dat
        :param nr: id dat
        :type nr: str
        :param modified_problem: show-ul cu datele noi
        :type modified_problem: Serial
        :return: show-ul modificat
        :rtype: Serial
        :raises: ShowNotFoundException daca nu exista serial cu id dat
        """

        all_problems = self.__load_from_file()
        index = self.__find_index(all_problems, nr)
        if index == -1:
            raise PbLabNotFoundException()

        all_problems[index] = modified_problem

        self.__save_to_file(all_problems)
        return modified_problem

    def delete_all(self):
        self.__save_to_file([])
