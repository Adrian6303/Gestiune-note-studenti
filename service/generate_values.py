from domain.entities import Student
from domain.entities import PbLaborator
from domain.validators import Validator
from repository.student_repo import StudentFileRepo

import random
import string


class Random:

    def __init__(self, repoS, repoL, validator):
        """
        Initializeaza service
        :param repo: obiect de tip repo care ne ajuta sa gestionam multimea de studenti si probleme
        :type repo: InMemoryRepository
        :param validator: validator pentru verificarea datelor
        :type validator:
        """
        self.__repoS = repoS
        self.__repoL = repoL
        self.__validator = validator

    def random_student(self):
        """
                Student random
                :return: obiectul de tip Student generat random
                :rtype Student
        """

        student_id = random.randint(100000, 999999)
        nr_grupa = random.randint(1, 99)
        letters = string.ascii_lowercase
        len = random.randint(5, 20)
        nume = ''.join(random.choice(letters) for i in range(len))
        s = Student(student_id, nume, nr_grupa)

        self.__repoS.store(s)
        return s

    def random_pbLab(self):
        """
                Problema random
                :return: obiectul de tip PbLaborator generat random
                :rtype PbLaborator
        """

        nr_lab = random.randint(1, 20)
        nr_pb = random.randint(1, 99)
        NrLab_nrPb = str(nr_lab) + '_' + str(nr_pb)
        day = random.randint(1, 29)
        letters = string.ascii_lowercase
        len = random.randint(5, 30)
        descriere = ''.join(random.choice(letters) for i in range(len))
        months = ['ianuarie', 'februarie', 'martie', 'aprilie', 'mai', 'iunie', 'iulie', 'august', 'septembrie',
                  'octombrie', 'noiembrie', 'decemrie']
        nr_m = random.randint(0, 11)
        deadline = str(day) + ' ' + str(months[nr_m])

        p = PbLaborator(NrLab_nrPb, descriere, deadline)

        self.__repoL.store(p)
        return p
