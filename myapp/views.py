from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<H1>index</H1>")


def hello(request):
    return HttpResponse("<H1>hello</H1>")