from django.shortcuts import render
from .models import News


# Create your views here.

def print_post(request):
    obj_list = News.objects.all()
    return render(request, './index.html', {'obj_list': obj_list})

