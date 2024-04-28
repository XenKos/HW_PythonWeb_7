from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, Grade

# Створення підключення до бази даних SQLite
engine = create_engine('sqlite:///C:\\Users\\Денег на комп нету\\OneDrive\\Робочий стіл\\Database_HW_Python_6.db')

# Створення сесії
Session = sessionmaker(bind=engine)
session = Session()