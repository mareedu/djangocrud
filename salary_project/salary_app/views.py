from django.shortcuts import render ,redirect
from salary_app.models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'salary_app/index.html', context)

def create(request):
    student = Student(name=request.POST['name'], company=request.POST['company'], salary=request.POST['salary'],)
    student.save()
    return redirect('/salary_app/')

def edit(request, id):
    student = Student.objects.get(id=id)
    context = {'student': student}
    return render(request, 'salary_app/edit.html', context)

def update(request, id):
    student = Student.objects.get(id=id)
    student.name = request.POST['name']
    student.company = request.POST['company']
    student.salary = request.POST['salary']
    student.save()
    return redirect('/salary_app/')

def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/salary_app/')
