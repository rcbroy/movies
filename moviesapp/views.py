from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .tmdb import TMDB

tmdb = TMDB()
def home(request):
    return render(request, 'moviesapp/home.html', {})

def movies(request):
    results = tmdb.movie_search("star wars")
    print(type(results))
    # data = simplejson.dumps(results)
    return JsonResponse(results)
    # return HttpResponse(data, content_type='application/json')

def results(request):
    query = request.GET['query']
    response = tmdb.movie_search(query)
    return render(request, 'moviesapp/results.html', response)