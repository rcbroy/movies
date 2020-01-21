import requests
from . import key

class TMDB:
    def __init__(self):
        self._API_KEY = key.API_KEY
        self.base_url = "https://api.themoviedb.org/3"

    def _tmdb_request(self, search_url, query=""):
        request_url = self.base_url + search_url
        payload = {'api_key': self._API_KEY}
        if query:
            payload['query'] = query
        response = requests.get(request_url, params=payload)
        return response.json()

    def _search(self, search_type, query):
        search_url = '/search/' + search_type
        response = self._tmdb_request(search_url, query)
        #results = response['results']
        return response

    def _movie(self, movie_id):
        pass

    def movie_search(self, query):
        return self._search('movie', query)

    def people_search(self, query):
        return self._search('people', query)

    def tv_search(self, query):
        pass

    def movie_get_details(self, movie_id):
        pass

    def people_get_details(self, person_id):
        pass

    def tv_get_details(self, tv_id):
        pass