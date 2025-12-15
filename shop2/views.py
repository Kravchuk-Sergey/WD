from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! Дякую, що відвідав нас, приємно тебе бачити!")