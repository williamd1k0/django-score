import json

from django.conf import settings
from django.http import HttpResponse, JsonResponse

from .utils import has_token, has_score_data
from .models import ScoreData

# Create your views here.

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
