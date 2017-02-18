from django.conf import settings
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Game Sample index")


def pong(request):
    print(request.is_ajax())
    print(request.method)
    if settings.DEBUG:
        REQUEST = request.GET
    else:
        REQUEST = request.POST
    response = REQUEST.get("ping", False)
    if response:
        return HttpResponse("Pong")
    return HttpResponse("")