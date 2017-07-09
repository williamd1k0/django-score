import json

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse

from .models import ScoreData


# Create your views here.

class HttpResponseUnauthorized(HttpResponse):
    status_code = 401


def get_score_data(body: bytes):
    if body != b'':
        try:
            data = json.loads(body.decode('utf-8'))
        except ValueError:
            return None
        return data if 'name' in data and 'points' in data else None
    return None

def is_token_valid(request):
    return request.META.get('HTTP_CLIENT_TOKEN', None) == settings.GAME_TOKEN

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
        data = get_score_data(request.body)
        if data is not None:
            return function(request, data, *args, **kwargs)
        else:
            print('NO SCORE DATA RECEIVED')
            return HttpResponseBadRequest()
    return wrap


@has_token
def index(request):
    return HttpResponse("Token test: Ok")


@has_token
@has_score_data
def new_score_entry(request, data):
    print(data['name'], data['points'])
    score = ScoreData(name=data['name'], points=data['points'])
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
