from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 
def home_screen(request):
    return HttpResponse('<h1>Hello World</h1')

def contact_page(request):
    return HttpResponse('<h1>This is the contact page</h1>')