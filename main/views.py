from django.shortcuts import render, HttpResponse

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')

def second(request):
    return HttpResponse('This is page test2')

def third(request):
    return HttpResponse('This is page test3')
    
def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

def page3(request):
    return render(request, 'page3.html')