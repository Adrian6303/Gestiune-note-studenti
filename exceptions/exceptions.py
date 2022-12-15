class ShowManagerException(Exception):
    pass


class ValidationException(ShowManagerException):
    def __init__(self, msgs):
        """
        :param msgs: lista de mesaje de eroare
        :type msgs: msgs
        """
        self.__err_msgs = msgs

    def getMessages(self):
        return self.__err_msgs

    def __str__(self):
        return 'Validation Exception: ' + str(self.__err_msgs)


class RepositoryException(ShowManagerException):
    def __init__(self, msg):
        self.__msg = msg

    def getMessage(self):
        return self.__msg

    def __str__(self):
        return 'Repository Exception: ' + str(self.__msg)


class DuplicateIDException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "ID duplicat.")


class GradeAlreadyAssignedException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Grade existent deja pentru un student si problema data.")


class StudentNotFoundException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Studentul nu a fost gasit.")


class GradeNotFoundException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Rating-ul nu a fost gasit.")


class PbLabNotFoundException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Problema de Laborator nu a fost gasita.")

class NotEnoughGradesException(ShowManagerException):
    def __init__(self):
        pass
class DuplicateIDException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "ID-ul exista deja.")

class DuplicateNrException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Nr-ul exista deja.")
