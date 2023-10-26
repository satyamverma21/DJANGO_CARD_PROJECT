from django.contrib import admin
from .models import *
from django.db.models import Sum

# Register your models here.

admin.site.register(Subject)

class SubjectmarksAdmin(admin.ModelAdmin):
    list_display = ['student','subject','marks']
    
admin.site.register(SubjectMarks, SubjectmarksAdmin) 
admin.site.register(Student)   
admin.site.register(StudentID)   
admin.site.register(Department)   

class RanklistAdmin(admin.ModelAdmin):
    list_display = ['student','student_rank','total_marks' , 'report_card_date']
    ordering = ['student_rank']
    def total_marks(self, obj):
        subject_marks = SubjectMarks.objects.filter(student=obj.student)
        marks = subject_marks.aggregate(marks=Sum('marks'))['marks']
        return marks
        
admin.site.register(Ranklist, RanklistAdmin)    
    