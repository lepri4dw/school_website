from django.shortcuts import render
from .models import Teacher

def get_teachers(request, category=None):
    if category:
        teachers = Teacher.objects.filter(category=category)
    else:
        teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers, 'category': category})
