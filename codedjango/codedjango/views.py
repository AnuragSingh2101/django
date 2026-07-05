from django.http import HttpResponse
from django.shortcuts import render


# You can also use render to serve HTML templates if needed
def home(request):
    return render(request, 'website/index.html')


# def home(request):
#     return HttpResponse("Welcome to CodeDjango!")


def about(request):
    return HttpResponse("About CodeDjango")


def contact(request):
    return HttpResponse("Contact us at 8452824226")


def services(request):
    return HttpResponse("Our Services include web development, app development, and more.")

