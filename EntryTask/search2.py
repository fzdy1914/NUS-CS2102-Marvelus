from django.shortcuts import render
from django.views.decorators import csrf


def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['out']
    return render(request, "post.html", ctx)
