from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, Grade
from sqlalchemy import func

engine = create_engine('sqlite:///C:\\Users\\Денег на комп нету\\OneDrive\\Робочий стіл\\Database_HW_Python_6.db')

Session = sessionmaker(bind=engine)
session = Session()

# Функція для знаходження 5 студентів із найбільшим середнім балом з усіх предметів
def select_1():
    return session.query(Student).order_by(func.avg(Grade.grade)).limit(5).all()

# Функція для знаходження студента із найвищим середнім балом з певного предмета
def select_2(subject_name):
    return session.query(Student).join(Grade).join(Subject).filter(Subject.subject_name == subject_name).group_by(Student.id).order_by(func.avg(Grade.grade)).first()

# Функція для знаходження середнього балу у групах з певного предмета
def select_3(subject_name):
    return session.query(Group.group_name, func.avg(Grade.grade)).join(Student).join(Grade).join(Subject).filter(Subject.subject_name == subject_name).group_by(Group.group_name).all()

# Функція для знаходження середнього балу на потоці (по всій таблиці оцінок)
def select_4():
    return session.query(func.avg(Grade.grade)).scalar()

# Функція для знаходження курсів, які читає певний викладач
def select_5(teacher_name):
    return session.query(Subject.subject_name).join(Teacher).filter(Teacher.teacher_name == teacher_name).all()

# Функція для знаходження списку студентів у певній групі
def select_6(group_name):
    return session.query(Student).join(Group).filter(Group.group_name == group_name).all()

# Функція для знаходження оцінок студентів у окремій групі з певного предмета
def select_7(group_name, subject_name):
    return session.query(Student.name, Grade.grade).join(Grade).join(Subject).join(Group).filter(Group.group_name == group_name, Subject.subject_name == subject_name).all()

# Функція для знаходження середнього балу, який ставить певний викладач зі своїх предметів
def select_8(teacher_name):
    return session.query(func.avg(Grade.grade)).join(Subject).join(Teacher).filter(Teacher.teacher_name == teacher_name).scalar()

# Функція для знаходження списку курсів, які відвідує певний студент
def select_9(student_name):
    return session.query(Subject.subject_name).join(Grade).join(Student).filter(Student.name == student_name).distinct().all()

# Функція для знаходження списку курсів, які відвідує певний студент від певного викладача
def select_10(student_name, teacher_name):
    return session.query(Subject.subject_name).join(Grade).join(Student).join(Teacher).filter(Student.name == student_name, Teacher.teacher_name == teacher_name).distinct().all()