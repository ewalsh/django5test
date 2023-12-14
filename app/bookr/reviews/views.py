from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = request.GET.get('name') or 'world'
    # return HttpResponse('Hello {}'.format(name))
    return(
        render(request, 'base.html', {'name': name})
    )
