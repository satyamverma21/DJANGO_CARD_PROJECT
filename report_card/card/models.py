from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.department

    class Meta:
        ordering = ['department']

class StudentID(models.Model):
    student_id = models.CharField(max_length=100)
    
    def __str__(self):
        return self.student_id 
    
    
class Student(models.Model):
    department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID, unique=True, related_name="studentId", on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()
    
    def __str__(self):
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = "student"

    
class Subject(models.Model):   
    subject_name = models.CharField(max_length=100)   
    
     
    def __str__(self):
        return self.subject_name
     
    

class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, related_name="studentmarks", on_delete=models.CASCADE) 
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE) 
    marks = models.IntegerField()
    
    def __str__(self):
        return f"{self.student.student_name}, {self.subject.subject_name}"

    class Meta:
        unique_together = ['subject', 'student']    
        

class Ranklist(models.Model):
 
    student = models.ForeignKey(Student, related_name="studentranklist", on_delete=models.CASCADE) 
    student_rank = models.IntegerField()
    report_card_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['student_rank', 'report_card_date']
    