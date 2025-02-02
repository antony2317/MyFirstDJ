from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html', {'questions': questions})
