from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from django.db.models import Q, Sum

# Create your views here.
def get_ranking(student_id):
    ranks = Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks', 'student_age')
    student_rank = -1 
    for i, rank in enumerate(ranks):
        if student_id == rank.student_id.student_id:
            student_rank = i+1
            break
    return student_rank

def student_page(request):
    
    queryset = Student.objects.all()
    search = request.GET.get('search', None)  
    pagination_size = 15
    
    if search:
        
        query = (
            Q(student_name__icontains = search) | 
            Q(student_age__icontains = search) | 
            Q(student_id__student_id__icontains = search) | 
            Q(department__department__icontains = search) |
            Q(student_email__icontains = search)     
        )
        pagination_size = 1000
        queryset = Student.objects.filter(query)
    
    paginator = Paginator(queryset,pagination_size)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    student_ranking = [(s,get_ranking(s.student_id.student_id)) for s in page_obj.object_list]
    context= {"page_obj": page_obj, "current_page":page_number,"ranklist": student_ranking, "page": "Student" }
    return render(request, "student.html", context= context)


def report_page(request, student_id): 
    
    queryset = SubjectMarks.objects.filter(student__student_id__student_id=student_id) 
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    context = {"queryset": queryset, "page": "report",  "total_marks": total_marks}
 
    return render(request, "report.html", context=context)
    
    
