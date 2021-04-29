from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from django.core import serializers

# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        number = request.POST['number']
        student_create = Student.objects.create(name=name,number=number)
        data = {'student_create':serializers.serialize('json',[student_create])}
        return JsonResponse(data)
    else:
        student_details = Student.objects.all()
        context = {'student_details':student_details}
        return render(request, 'student.html',context)