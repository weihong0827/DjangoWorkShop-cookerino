from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Recipes
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def image_api(request):
    
    if request.method != 'POST':
        return HttpResponse('Error 403',status = 403)
    data = request.body.decode('utf-8')
    
    info = json.loads(data)
 
    use = info['usage']
    ingredients = info['ingredients']
    if use == 'product_img':
        filepath = Recipes.objects.filter(ingredients=ingredients)[0].product_img
        with open(filepath,'rb') as f:
            byte = f.read()
            print(type(byte))
            return HttpResponse(byte,status =200)