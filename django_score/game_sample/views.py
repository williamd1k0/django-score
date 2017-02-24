from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse

from .models import ScoreData


# Create your views here.

class HttpResponseUnauthorized(HttpResponse):
    status_code = 401

defaut_request = lambda request: request.GET if settings.DEBUG else request.POST

def is_token_valid(request):
    return defaut_request(request).get('token', None) == settings.GAME_TOKEN

# Wrapper for token validation
def has_token(function):
    def wrap(request, *args, **kwargs):
        if is_token_valid(request):
            print('TOKEN OK')
            return function(request, *args, **kwargs)
        else:
            print('BAD TOKEN')
            return HttpResponseUnauthorized()
    return wrap

# Wrapper for score data validation
def has_score_data(function):
    def wrap(request, *args, **kwargs):
        req = defaut_request(request)
        if not None in (req.get('name'), req.get('points')):
            return function(request, req.get('name'), req.get('points'), *args, **kwargs)
        else:
            print('NO SCORE DATA RECEIVED')
            return HttpResponseBadRequest()
    return wrap


@has_token
def index(request):
    return HttpResponse("Token test: Ok")


@has_token
@has_score_data
def new_score_entry(request, name, points):
    print(name, points)
    score = ScoreData(name=name, points=points)
    score.save()
    return HttpResponse('OK')


@has_token
def get_score_list(request):
    # Simple data serialization
    score_list = [
        {
            'name': score.name,
            'points': score.points
        } for score in ScoreData.objects.all()
    ]
    return JsonResponse({'score_list': score_list})
