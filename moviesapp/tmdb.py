import requests
from . import key

class TMDB:
    def __init__(self):
        self._API_KEY = key.API_KEY
        self.base_url = "https://api.themoviedb.org/3"

    def _tmdb_request(self, request_type, query="", page=1):
        """
        """
        request_url = self.base_url + request_type
        payload = {'api_key': self._API_KEY}
        if query:
            payload['query'] = query
        payload['page'] = page
        response = requests.get(request_url, params=payload)
        return response.json()

    def now_playing(self, page=1):
        request_type = "/movie/now_playing"
        response = self._tmdb_request(request_type)
        return response
        
    def _search(self, search_type, query, page):
        search_url = '/search/' + search_type
        response = self._tmdb_request(search_url, query, page)
        #results = response['results']
        return response

    def _movie(self, movie_id):
        pass

    def movie_search(self, query, page=1):
        return self._search('movie', query, page)

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