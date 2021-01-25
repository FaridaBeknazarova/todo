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

def delete_todo(request, id):
    todo=ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo=ToDo.objects.get(id=id)
    todo.is_favorite=True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo=ToDo.objects.get(id=id)
    todo.is_favorite=False
    todo.save()
    return redirect(test)





def add_book(request):
    form_item=request.POST
    item=Book(
        title=form_item["book_title"],
        subtitle=form_item["book_subtitle"],
        description=form_item["book_description"],
        price=form_item["book_price"],
        genre=form_item["book_genre"],
        author=form_item["book_author"],
        year=form_item["book_year"][:10]
    )
    item.save()
    return redirect(second)


def delete_book(request, id):
    item=Book.objects.get(id=id)
    item.delete()
    return redirect(second)

def mark_book(request, id):
    item=Book.objects.get(id=id)
    item.is_favorite=True
    item.save()
    return redirect(second)

def unmark_book(request, id):
    item=Book.objects.get(id=id)
    item.is_favorite=False
    item.save()
    return redirect(second)
    