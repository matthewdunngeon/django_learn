import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): #*args, **kwargs
    return HttpResponse("Hello, Django!")

def contact_view(*args, **kwargs): #*args, **kwargs
    return HttpResponse("<h1>Contact Page</h1>")

def about_view(*args, **kwargs): #*args, **kwargs
    return HttpResponse("<h1>About Page</h1>")

def social_view(*args, **kwargs): #*args, **kwargs
    return HttpResponse("<h1>Social Page</h1>")

# for testing url
print("http://127.0.0.1:8000/hello/Matthew\n")

def hello_there_view(request, name):
        return render(
        request,
        'pages/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def hello_there2_view(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)