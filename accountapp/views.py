from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):
    if request.method == "POST":
        return render(request, 'accountapp/hello_newworld.html',
                      context={'text': 'POST METHOD'})
    else:
        return render(request, 'accountapp/hello_newworld.html',
                      context={'text': 'GET METHOD'})