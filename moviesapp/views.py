from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .tmdb import TMDB

tmdb = TMDB()
def home(request):
    response = tmdb.now_playing()
    return render(request, 'moviesapp/home.html', response)

def movies(request):
    results = tmdb.movie_search("star wars")
    print(type(results))
    # data = simplejson.dumps(results)
    return JsonResponse(results)
    # return HttpResponse(data, content_type='application/json')

def results(request):
    query = request.GET['query']
    page = request.GET['page']
    response = tmdb.movie_search(query, page)
    response['query'] = query
    return render(request, 'moviesapp/results.html', response)