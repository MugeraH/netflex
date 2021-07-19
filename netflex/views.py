from django.shortcuts import render
from .request import get_trending_movies,get_popular_movies

def home(request):
    # print(len(get_trending_movies()))
    trending_movies = get_trending_movies()
    popular_movies = get_popular_movies()
    
    movie_highlight=(trending_movies[:1])[0]
    movies_trending = trending_movies[1:]
    
    # print(movie_highlight['title'])
   
    ctx={
        
        "movie_highlight":movie_highlight,
        "movies_trending":movies_trending,
        "popular_movies": popular_movies
      
    }
    return render(request,"netflex/home.html",ctx)

def single_movie(request,movie_id):
    print(movie_id)
    return render(request)

