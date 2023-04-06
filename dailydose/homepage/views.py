from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Email
from django.http import JsonResponse
import json
from homepage.utils import fetch_news
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.staticfiles import finders


# Create your views here.
def index(request):
    return render(request, 'index.html')


def save_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data['email']
        choices = data['choices']
        email_obj = Email(email=email, choices=choices)
        email_obj.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
    

def news(request):
    if request.method=='POST':
        fetch_news()
        return redirect(reverse('admin:index'))
    return render(request, 'news.html')


def serve_css(request):
    # find the path to the CSS file
    path = finders.find('style.css')
    
    # read the contents of the CSS file
    with open(path, 'r') as f:
        css_file = f.read()
    
    # create an HTTP response with the CSS file and set the content type
    response = HttpResponse(css_file, content_type='text/css')
    
    return response
