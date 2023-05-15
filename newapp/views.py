from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    resp = '''<h1>NewApp</h1>
    <p>Fourth day</p>

    '''
    return HttpResponse(resp)


def Second(request):
    resp = '''<h1>Second Page</h1>
    <p>I am learning python programming</p>

    '''
    return HttpResponse(resp)


def third(request):
    resp = '''<h1>Third</h1>
    <p>I am learning python programming</p>

    '''
    return HttpResponse(resp)
