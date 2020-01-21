from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .tmdb import TMDB

def home(request):
    return HttpResponse("hello movies")

def movies(request):
    tmdb = TMDB()
    results = tmdb.movie_search("star wars")
    # data = simplejson.dumps(results)
    return JsonResponse(results)
    # return HttpResponse(data, content_type='application/json')