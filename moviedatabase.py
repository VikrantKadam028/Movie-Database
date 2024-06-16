import requests
import json

# main_api = "https://api.themoviedb.org/3/movie/157336?api_key=797418d57bb2c545a77688f41fceeec3"
# search_api = "https://api.themoviedb.org/3/search/movie"
# now_playing = "https://api.themoviedb.org/3/movie/now_playing"
# top_rated = "https://api.themoviedb.org/3/movie/top_rated"
# upcoming = "https://api.themoviedb.org/3/movie/upcoming"

def search_movie():
    i = 0
    search_m = input("Enter the movie name to search :")
    url1 = f"https://api.themoviedb.org/3/search/movie?api_key=797418d57bb2c545a77688f41fceeec3&&query={search_m}"
    search_req = requests.get(url1)
    search_dic = json.loads(search_req.text)
    if 'results' in search_dic:
        for movie in search_dic['results']:
            print(f"Title: {movie.get('original_title')}")
            print(f"Release Date: {movie.get('release_date')}")
            print(f"Original language: {movie.get('original_language')}")
            print()
            i = i + 1
            print("-" * 30)
        print(f"{i} results found.")            
    else:
        print("No results found.")
        
def now_playing():
    k = 0
    url2 = "https://api.themoviedb.org/3/movie/now_playing?api_key=797418d57bb2c545a77688f41fceeec3"
    play_req = requests.get(url2)
    play_dict = json.loads(play_req.text)
    if 'results' in play_dict:
        for movie in play_dict['results']:
            print(f"Title :{movie.get('original_title')}")
            print(f"id :{movie.get('id')}")
            print(f"Popularity :{movie.get('popularity')}")
            print(f"Release Date :{movie.get('release_date')}")
            k = k + 1
            print("-"*35)
        print(f"{k} results found.")      
    else:
        print("Movies are not currently playing!")    

def top_rated():
    j = 0
    url3 = "https://api.themoviedb.org/3/movie/top_rated?api_key=797418d57bb2c545a77688f41fceeec3"
    rated_req = requests.get(url3)
    rated_dict = json.loads(rated_req.text)
    if 'results' in rated_dict:
        for movie in rated_dict['results']:
            print(f"Title :{movie.get('original_title')}")
            print(f"id :{movie.get('id')}")
            print(f"Popularity :{movie.get('popularity')}")
            print(f"Release Date :{movie.get('release_date')}")
            j = j + 1
            print("-"*35)
        print(f"{j} results found.")      
    else:
        print("Movies are not currently playing!")

def up_coming():
    u = 0
    url4 = "https://api.themoviedb.org/3/movie/upcoming?api_key=797418d57bb2c545a77688f41fceeec3"
    up_req = requests.get(url4)
    up_dict = json.loads(up_req.text)
    if 'results' in up_dict:
        for movie in up_dict['results']:
            print(f"Title :{movie.get('original_title')}")
            print(f"id :{movie.get('id')}")
            print(f"Popularity :{movie.get('popularity')}")
            print(f"Release Date :{movie.get('release_date')}")
            u = u + 1
            print("-"*35)
        print(f"{u} results found.")      
    else:
        print("Movies are not currently playing!")


print("*********************")
print("The World Of Movies!🎥")
print("*********************")

movie_choice = int(input(("1.Search Movie\n2.Now playing\n3.Top rated\n4.Upcoming\n5.Exit\nEnter your choice :")))
print()
match movie_choice:
    case 1:
        search_movie()
    case 2:
        now_playing()
    case 3:
        top_rated()
    case 4:
        up_coming()
      
    case _:
        print("Invalid input!!")
