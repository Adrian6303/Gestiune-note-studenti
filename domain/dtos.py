class PbLabStudentGrade:
    def __init__(self, studentId, nrPb, grade):
        # fields: studentId, nrPb, grade
        self.__studentId = studentId
        self.__nrPb = nrPb
        self.__grade = grade

    def getStudentId(self):
        return self.__studentId

    def getNrPb(self):
        return self.__nrPb

    def getrGrade(self):
        return self.__grade

    def setStudentId(self, value):
        self.__studentId = value

    def setNrPb(self, value):
        self.__nrPb = value

    def setGrade(self, value):
        self.__grade = value
