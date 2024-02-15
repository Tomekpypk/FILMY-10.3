import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3OTI1MTgwYzQxZjVlZTMzMWNlMThmOGZkOWU4Mzk3MyIsInN1YiI6IjY1Y2I5MmM0ZjkyNTMyMDE2M2MwMzU5YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.FHt9fRxVMgWaDpFIAmbUrrcpNwk19gc5nZuO92yQ7dw"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"
