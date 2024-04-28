
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, Grade
from datetime import datetime, timedelta

engine = create_engine('sqlite:///C:\\Users\\Денег на комп нету\\OneDrive\\Робочий стіл\\Database_HW_Python_6.db')

Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

def create_students(n):
    for _ in range(n):
        student = Student(
            name=fake.name(),
            gender=fake.random_element(elements=('Male', 'Female')),
            date_of_birth=fake.date_of_birth(),
            email=fake.email()
        )
        session.add(student)

def create_groups(n):
    for _ in range(n):
        group = Group(
            group_name=fake.word().capitalize(),
            numbers_of_students=fake.random_number(digits=2),
            year_established=fake.year()
        )
        session.add(group)

def create_teachers(n):
    for _ in range(n):
        teacher = Teacher(
            teacher_name=fake.name(),
            position=fake.job(),
            email=fake.email()
        )
        session.add(teacher)

def create_subjects(n):
    for _ in range(n):
        subject = Subject(
            subject_name=fake.word().capitalize(),
            teacher_id=fake.random_int(min=1, max=n)
        )
        session.add(subject)

def create_grades(n):
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    for _ in range(n):
        student = fake.random_element(students)
        subject = fake.random_element(subjects)
        grade = Grade(
            student_id=student.id,
            subject_id=subject.id,
            grade=fake.random_int(min=1, max=100),
            date_received=fake.date_time_between(start_date='-4y', end_date='now')
        )
        session.add(grade)

create_students(50)
create_groups(3)
create_teachers(5)
create_subjects(8)
create_grades(20)

session.commit()