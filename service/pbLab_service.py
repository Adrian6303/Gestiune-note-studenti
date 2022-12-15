from domain.entities import PbLaborator
from domain.validators import Validator
from repository.pbLab_repo import PbLabFileRepo
from exceptions.exceptions import *






class PbLabService:
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
        self.__repo.store(p)
        return p

    def get_all_problems(self):
        """
        Returneaza o lista cu toate problemele disponibile
        :return: lista de probleme disponibile
        :rtype: list of objects de tip PbLaborator
        """
        return self.__repo.get_all()

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
        return self.__repo.delete(nr)

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
        return self.__repo.edit(nr, pb)

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
        return self.__repo.find(nr)



def test_add_probleme():
    repo = PbLabFileRepo()
    validator = Validator()
    test_srv = PbLabService(repo, validator)

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
