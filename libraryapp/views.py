from django.shortcuts import render
from django.template import loader
# Create your views here.

from django.http import HttpResponse
print("hello world")

def index(request):
    template = loader.get_template('index.html')
    return render(response , "index.html", {})

class BookCreateView:
    def post(self):
        pass

class BookDetailView:
    def get(self):
        pass

class BookListView:
    def get(self):
        pass
