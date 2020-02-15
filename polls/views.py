from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Group_Emotion as GE
# Create your views here.

def index(request):
    ge = GE(group="3", emotion="fear")
    ge.save()

    return HttpResponse("Hello Django!!")

def hello(request):
    return render(request, 'hello.html')