from domain.entities import Student
from exceptions.exceptions import *




class StudentFileRepo:
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
        all_students = []
        for line in lines:
            student_id, student_name, student_grupa = [token.strip() for token in line.split(';')]
            student_id = int(student_id)
            student_grupa = int(student_grupa)

            s = Student(student_id, student_name, student_grupa)
            all_students.append(s)

        f.close()
        return all_students

    def __save_to_file(self, all_students):
        """
        Salveaza studenti in fisier
        """
        with open(self.__filename, 'w') as f:
            for student in all_students:
                student_string = str(student.getStudentID()) + ';' + str(student.getNume()) + ';' + str(
                    student.getGrup()) + '\n'
                f.write(student_string)

    def find(self, id):
        """
        Cauta studentul cu id dat
        :param id: id dat
        :type id: str
        :return: student cu id dat, None daca nu exista serial cu id dat
        :rtype: Student
        """
        all_students = self.__load_from_file()
        for student in all_students:
            if student.getStudentID() == id:
                return student
        return None

    def store(self, student):
        """
       Adauga un serial in lista
       :param student: studentul care se adauga
       :type student: Student
       :return: -; lista de studenti se modifica prin adaugarea studentului dat
        :rtype:
        :raises: DuplicateIDException daca studentul exista deja
        """
        all_students = self.__load_from_file()
        if student in all_students:
            raise DuplicateIDException()

        all_students.append(student)
        self.__save_to_file(all_students)

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

    def __find_index(self, all_students, id):
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
        for i in range(len(all_students)):
            if all_students[i].getStudentID() == id:
                index = i

        return index

    def delete(self, id):
        """
        Sterge student dupa id
        :param id: id-ul dat
        :type id: str
        :return: studentul sters
        :rtype: Student
        :raises: StudentNotFoundException daca id-ul nu exista
        """
        all_students = self.__load_from_file()
        index = self.__find_index(all_students, id)
        if index == -1:
            raise StudentNotFoundException()

        deleted_student = all_students.pop(index)

        self.__save_to_file(all_students)
        return deleted_student

    def edit(self, id, modified_student):
        """
        Modifica datele serialului cu id dat
        :param id: id dat
        :type id: str
        :param modified_show: show-ul cu datele noi
        :type modified_show: Serial
        :return: show-ul modificat
        :rtype: Serial
        :raises: ShowNotFoundException daca nu exista serial cu id dat
        """

        all_students = self.__load_from_file()
        index = self.__find_index(all_students, id)
        if index == -1:
            raise StudentNotFoundException()

        all_students[index] = modified_student

        self.__save_to_file(all_students)
        return modified_student

    def delete_all(self):
        self.__save_to_file([])
