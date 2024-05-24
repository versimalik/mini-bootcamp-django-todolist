from django.shortcuts import render, HttpResponse

# Create your views here.

def welcome(request, name):
    return HttpResponse(f"Welcome, {name}")