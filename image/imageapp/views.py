from django.shortcuts import render
from django.http import HttpResponse,JsonResponse #new
from .models import Book
from django.template import loader 
from .forms import *
from django.shortcuts import redirect

def index(request): #new
    template = loader.get_template('index.html')
    books = Book.objects.all()
    context = {
        'books': books
    }
    return HttpResponse(template.render(context, request))

def upload_image(request): #new
    template = loader.get_template('upload.html')
    if request.method == 'POST':
        
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = BookForm()
            context = {
                'form': form
            }
            
            return redirect('/')
        
    else:
        form = BookForm()
        context = {
            'form': form
        }
        return HttpResponse(template.render(context, request))
    
def get_data(request):
    data = {'message': 'Hello, World!'}
    return JsonResponse(data)