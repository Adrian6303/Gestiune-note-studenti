from domain.validators import Validator
from ui.console import Console
from service.generate_values import Random
from repository.student_repo import StudentFileRepo
from service.student_service import StudentService
from service.pbLab_service import PbLabService
from repository.pbLab_repo import PbLabFileRepo
from repository.grade_repo import GradeFileRepo
from service.grade_service import GradeService

repoS = StudentFileRepo('data/students.txt')
repoL = PbLabFileRepo('data/pbLab.txt')
repoG = GradeFileRepo('data/grades.txt')

val = Validator()

srvL = PbLabService(repoL, val)
srvS = StudentService(repoS, val)
srvR = Random(repoS, repoL, val)
srvG = GradeService(repoS, repoL, repoG, val)

ui = Console(srvL, srvS, srvR, srvG)
ui.gestiune_lab_ui()
