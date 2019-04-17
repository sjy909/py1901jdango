from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Book_list

def index(request):
    return HttpResponse("index")


def list(request):
    return HttpResponse("列表")


def detail(request, a):
    try:
        d = Book_list.objects.get(pk=a).book_name
        return HttpResponse(d)
    except:
        return HttpResponse("ID错误")
