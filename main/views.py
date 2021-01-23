from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Book

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def test(request):
    todo_list=ToDo.objects.all()
    return render(request, 'test.html', {"todo_list":todo_list})

def second(request):
    book_item=Book.objects.all()
    return render(request, 'books.html', {"book_item":book_item})

def third(request):
    return HttpResponse('This is page test3')
    
def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

def page3(request):
    return render(request, 'page3.html')

def add_todo(request):
    form=request.POST
    text=form["todo_text"]
    todo=ToDo(text=text)
    todo.save()
    return redirect(test)

def add_book(request):
    form_item=request.POST
    title=form_item["book_title"]
    i=Book(title=title)
    i.save()
    return redirect(second)

def delete_todo(request, id):
    todo=ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)
    
    