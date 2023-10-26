from faker import Faker
from .models import * 
from django.db.models import Sum
import random

fake = Faker()

def seed_student_db(n=10):
    try:
        ids = (f"{id:03}" for id in sorted(range(0,999), key=lambda x: random.random()))   
        for i in range(0, n):

            departments_objs = Department.objects.all()
            random_index = random.randint(0, len(departments_objs)-1)
            department = departments_objs[random_index]
            student_id = f"STU-0{next(ids)}"
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20,30)
            student_address = fake.address()
            
            student_id_obj = StudentID.objects.create(student_id=student_id)
            
            Student.objects.create(
                department = department ,
                student_id = student_id_obj ,
                student_name = student_name ,
                student_email = student_email ,
                student_age = student_age ,
                student_address = student_address 
            )
            
    except Exception as e:
        print(f"[Error]: {e}")
    

def seed_subject_db():
    try:
        student_obj = Student.objects.all()
        for student in student_obj:
            subjects = Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    subject=subject,
                    student=student,
                    marks=random.randint(10,100) 
                )
                
    except Exception as e:
        print(f"[Error]: {e}")
    
        
def seed_ranklist():
    try:
        sorted_students = Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks', 'student_age')
        for i, student_name in enumerate(sorted_students):
            Ranklist.objects.create(
                student = student_name,
                student_rank = i+1
            )
            
    except Exception as e:
        print(f"[Error]: {e}")


def seed_db(n=10):
    seed_student_db(n)
    seed_subject_db()
