from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello,  New User!")


def hello_there(request, username):
    return render(
        request,
        'homework_6/greeting.html',
        {
            'username': username,
        }
    )
