from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello_world(request):  
    if request.method == "POST":
    
        return render(request, 'accountapp/hello_world.html', context={'text':'post method'})
    else:

        return render(request, 'accountapp/hello_world.html', context={'text':'get method'})