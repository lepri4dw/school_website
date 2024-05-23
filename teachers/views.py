from django.shortcuts import render, get_object_or_404
from .models import Teacher

def get_teachers(request, category=None):
    if category:
        teachers = Teacher.objects.filter(category=category)
    else:
        teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers, 'category': category})

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'teacher_detail.html', {'teacher': teacher})
