from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from .models import Book_list, Roles_list
from django.template import loader


def index(request):
    # indexhtml = loader.get_template("booktest/index.html")
    # cont = {"username": "sjy"}
    # result = indexhtml.render(cont)
    # return HttpResponse(result)
    return render(request, "booktest/index.html", {"username": "sy"})


def list(request):
    # return HttpResponse("列表")
    book_list = Book_list.objects.all()

    return render(request, "booktest/list.html", {"book_list": book_list})


def detail(request, a):
    # try:
    #     d = Book_list.objects.get(pk=a).book_name
    #     return HttpResponse(d)
    # except:
    #     return HttpResponse("ID错误")
    book_list = Book_list.objects.get(pk=a)
    cs = book_list.roles_list_set.all()
    return render(request, "booktest/detail.html", {"book_list": book_list, "cs": cs})


def delete(request, a):
    Book_list.objects.get(pk=a).delete()
    book_list = Book_list.objects.all()
    # return render(request, "booktest/list.html", {"book_list": book_list})
    return HttpResponseRedirect("/booktest/list", {"book_list": book_list})


def add(request):
    return render(request, "booktest/add.html")


def adds(request):
        bname = request.POST['bname']
        hname = request.POST['hname']
        b1 = Book_list()
        b1.book_name = hname
        b1.save()
        h1 = Roles_list()
        h1.role_name = bname
        h1.Roles_gerden = False
        h1.Roles_Book = b1
        h1.save()

        book_list = Book_list.objects.all()
        return HttpResponseRedirect("/booktest/list/", {"book_list": book_list})


def update(request, i):
    b1 = Book_list.objects.get(pk=i)
    print(type(b1.roles_list_set.all()))
    r = b1.roles_list_set.all()
    return render(request, "booktest/update.html", {"n": b1, "r": r})


def updates(request, i):
    b1 = Book_list.objects.get(pk=i)
    b1.book_name = request.POST["bname"]
    b1.save()
    r = b1.roles_list_set.all()
    for role in r:
        i = role.id
        i = str(i)
        role.role_name = request.POST[i]
        role.save()

    if request.POST["add"]:
        role = Roles_list()
        role.role_name = request.POST["add"]
        role.Roles_gerden = True
        role.Roles_Book = b1
        role.save()

    book_list = Book_list.objects.all()
    return HttpResponseRedirect("/booktest/list/", {"book_list": book_list})
