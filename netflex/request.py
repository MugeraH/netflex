from decouple import config
import requests 

api_key = config('API_KEY')


  
def get_trending_movies():
     get_trending_movies_url= f"https://api.themoviedb.org/3/trending/all/day?api_key={api_key}"
     movies_data = requests.get( get_trending_movies_url).json()["results"]      
          
     
     return movies_data
  

def get_popular_movies():
     get_popular_movies_url= f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1"
     movies_data = requests.get( get_popular_movies_url).json()["results"]      
          
     
     return movies_data



# /**
#  * This function searches for videos related to the keyword 'dogs'. The video IDs and titles
#  * of the search results are logged to Apps Script's log.
#  *
#  * Note that this sample limits the results to 25. To return more results, pass
#  * additional parameters as documented here:
#  *   https://developers.google.com/youtube/v3/docs/search/list
#  */
# function searchByKeyword() {
#   var results = YouTube.Search.list('id,snippet', {q: 'dogs', maxResults: 25});
#   for(var i in results.items) {
#     var item = results.items[i];
#     Logger.log('[%s] Title: %s', item.id.videoId, item.snippet.title);
#   }
# }




# https://api.themoviedb.org/3/trending/all/day?api_key=dfa8371a7b3cfdd34824897726f30634
# https://api.themoviedb.org/3/movie/{movie_id}?api_key=dfa8371a7b3cfdd34824897726f30634&language=en-US
