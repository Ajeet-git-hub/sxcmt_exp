from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from library.models import *
from django.contrib.auth import authenticate, login
from .forms import Work_form
# Create your views here.

def Front_look(request):
    book = Book.objects.order_by("-book_title")[:5]
    try:
        book = Book.objects.filter(book_title__contains = request.POST["find"])
        category = request.POST['options']
        if(category == "Title"):
            book = Book.objects.filter(book_title__contains = request.POST["find"])
        elif(category == "Publisher"):
            book = Book.objects.filter(book_publisher__contains = request.POST["find"])
        elif(category == "Author"):
            book = Book.objects.filter(book_author__contains = request.POST["find"])
    except:
        book = Book.objects.order_by("-book_title")[:5]
    return render(request, "library/front.html",{"book":book})
    
def Work_area(request):
    try:
        pass
    except:
        return render(request, "library/work.html", {})
    return render(request, "library/work.html", {})