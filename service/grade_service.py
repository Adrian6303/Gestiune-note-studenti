from domain.entities import Student, PbLaborator, Grade
from domain.validators import Validator
from repository.grade_repo import GradeFileRepo
from exceptions.exceptions import *





class GradeService:
    def __init__(self, repoS,repoL, repoG, validator):
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
        all_students= self.__repoS.get_all()
        ok=False
        for stud in all_students:
            media = 0
            nr = 0
            for grade in all_grades:
                if grade.getStudent() == stud.getStudentID():
                    media+=int(grade.getGrade())
                    nr+=1
            if nr>0:
                media=float(media/nr)
                if media < 5:
                    print("Studentul: "+ str(stud.getNume()) + "(ID: " + str(stud.getStudentID()) +"), media:" + str(media))
                    ok=True
        return ok

    def stat_studenti_note(self, nr):
        all_grades = self.__repoG.get_all()
        all_students = self.__repoS.get_all()
        studenti=[]
        ok=False
        for grade in all_grades:
            if grade.getPbLab() == nr:
                for student in all_students:
                    if student.getStudentID() ==grade.getStudent():
                        studenti.append(student.getNume())

        if len(studenti)>0:
            ok=True
            studenti = sorted(studenti)
            for stud in studenti:
                for grade in all_grades:
                    for student in all_students:
                        if student.getStudentID() == grade.getStudent():
                            if stud == student.getNume() and grade.getPbLab() == nr:
                                print('Studentul:' + str(stud) + ' cu nota: ' + str(grade.getGrade()))

        return ok

    def get_media_max(self):
        all_grades = self.__repoG.get_all()
        all_students = self.__repoS.get_all()
        ok = False
        max_medie=0

        for stud in all_students:
            media = 0
            nr = 0
            for grade in all_grades:

                if grade.getStudent() == stud.getStudentID():
                    media+=int(grade.getGrade())
                    nr+=1
            if nr>0:
                media=float(media/nr)
                if max_medie < media:
                    max_medie = float(media)
                    student = stud.getNume()
                    ok = True

        if ok==True:
            return f'Studentul:  {str(student)}  cu media:  {str(max_medie)}'
        return ok