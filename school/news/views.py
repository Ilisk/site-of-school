from django.shortcuts import render
from .models import News


# Create your views here.

def print(request):
    obj_list = News.objects.all()
    return render(request, './test.html', {'obj_list': obj_list})

