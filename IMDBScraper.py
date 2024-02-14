import requests
from bs4 import BeautifulSoup
from imdb import IMDb

def movie_search(title):
    mov = IMDb()
    movies = mov.search_movie(title)

    if not movies:
        print(f"No results found for '{title}'.")
        return None

    first_movie = movies[0]
    mov.update(first_movie)
    return first_movie

def get_rating(movie):
    if 'rating' in movie.data:
        return movie.data['rating']
    else:
        print("Rating not found.")
        return None

def get_genres(movie):
    if 'genres' in movie.data:
        return movie.data['genres']
    else:
        print("Genres not found.")
        return None

def get_plot_summary(movie):
    if 'plot' in movie.data:
        return movie.data['plot']
    else:
        print("Plot not found.")
        return None

def get_cast(movie):
    if 'cast' in movie.data:
        return movie.data['cast']
    else:
        print("Cast not found")
        return None

def main():
    movie_title = input("Enter the movie title: ")
    movie = movie_search(movie_title)

    if movie:
        print(f"Title: {movie['title']}")
        print(f"Year: {movie['year']}")
        
        imdb_rating = get_rating(movie)
        genres = get_genres(movie)
        plot = get_plot_summary(movie)
        cast = get_cast(movie)
        
        if imdb_rating:
            print(f"IMDB Rating: {imdb_rating}")
        if genres:
            print(f"Genres: {genres}")
        if plot:
            print(f"\nPlot Summary: {plot}")
        if cast:
            print("\nCast:")
            for people in cast:
                print(f"- {people['name']}")

if __name__ == "__main__":
    main()
