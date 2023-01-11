from domain.entities import Student, PbLaborator, Grade
from domain.validators import Validator
from repository.grade_repo import GradeFileRepo
from exceptions.exceptions import *
from service.sort import *

class GradeService:
    def __init__(self, repoS, repoL, repoG, validator):
        self.__repoS = repoS
        self.__repoL = repoL
        self.__repoG = repoG
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
        student = self.__repoS.find(student_id)
        if student is None:
            raise StudentNotFoundException()

        pb_lab = self.__repoL.find(pbLab_nr)

        if pb_lab is None:
            raise PbLabNotFoundException()

        grade = Grade(student_id, pbLab_nr, grade_val)
        self.__validator.validate_grade(grade)
        self.__repoG.store(grade)
        return grade

    def get_all_grades(self):
        return self.__repoG.get_all()

    def get_avg_sub5(self):
        all_grades = self.__repoG.get_all()
        all_students = self.__repoS.get_all()
        ok = False
        studenti=[]
        for stud in all_students:
            media = 0
            nr = 0
            for grade in all_grades:
                if grade.getStudent() == stud.getStudentID():
                    media += int(grade.getGrade())
                    nr += 1
            if nr > 0:
                media = float(media / nr)
                if media < 5:
                    studenti.append(stud)
                    ok = True
        if len(studenti) > 0:
            ok = True
            size = len(studenti)
            studenti = gnome_sort(studenti,lambda x:(x.getNume(), x.getStudentID()),False, cmp)
            print('Toti studenții cu media notelor de laborator mai mic decât 5:')
            for stud in studenti:
                for student in all_students:
                    if student.getStudentID() == stud.getStudentID():
                        print('Studentul: ' + str(student.getNume()) + ' (Id:' + str(student.getStudentID()) + ')')


        return ok

    def stat_studenti_note(self, nr):
        all_grades = self.__repoG.get_all()
        all_students = self.__repoS.get_all()
        studenti = []
        ok = False
        for grade in all_grades:
            if grade.getPbLab() == nr:
                for student in all_students:
                    if student.getStudentID() == grade.getStudent():
                        studenti.append(student)

        if len(studenti) > 0:
            ok = True
            studenti = quick_sort(studenti,lambda x:(x.getNume(), x.getStudentID()),False,cmp)
            print('Lista de studenți și notele lor la  problema de laborator ' + str(nr) + ' data:')
            for stud in studenti:
                for grade in all_grades:
                    for student in all_students:
                        if student.getStudentID() == grade.getStudent():
                            if stud.getStudentID() == student.getStudentID() and grade.getPbLab() == nr:
                                print('Studentul:' + str(student.getNume()) + ' (' + str(stud) + ') cu nota: ' + str(
                                    grade.getGrade()))

        return ok
    # varianta non- recursiva
    #
    # def get_media_max(self):
    #     all_grades = self.__repoG.get_all()
    #     all_students = self.__repoS.get_all()
    #     ok = False
    #     max_medie = 0
    #
    #     for stud in all_students:
    #         media = 0
    #         nr = 0
    #         for grade in all_grades:
    #
    #             if grade.getStudent() == stud.getStudentID():
    #                 media += int(grade.getGrade())
    #                 nr += 1
    #         if nr > 0:
    #             media = float(media / nr)
    #             if max_medie < media:
    #                 max_medie = float(media)
    #                 student = stud.getNume()
    #                 ok = True
    #
    #     if ok == True:
    #         return f'Studentul:  {str(student)}  cu media:  {str(max_medie)}'
    #     return ok

    def get_media_max(self, all_students = None, all_grades = None, max_medie=0, student=None):
        if not all_students:
            if max_medie > 0:
                return f'Studentul: {str(student)} cu media: {str(max_medie)}'
            all_students = self.__repoS.get_all()
            all_grades = self.__repoG.get_all()

        stud = all_students[0]
        media = 0
        nr = 0
        for grade in all_grades:
            if grade.getStudent() == stud.getStudentID():
                media += int(grade.getGrade())
                nr += 1
        if nr > 0:
            media = float(media / nr)
            if max_medie < media:
                max_medie = float(media)
                student = stud.getNume()

        return self.get_media_max(all_students[1:], all_grades, max_medie, student)

