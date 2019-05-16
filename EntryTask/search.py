from django.http import HttpResponse
from django.shortcuts import render_to_response



def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    request.encoding = 'utf-8'
    if 'in' in request.GET:
        message = 'Your searching: ' + request.GET['in']
    else:
        message = 'You have upload an empty chart'
    return HttpResponse(message)
