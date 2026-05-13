
movies = [
    {"title": "3 Idiots", "genre": "comedy drama education"},
    {"title": "Dangal", "genre": "drama sports biography"},
    {"title": "Sholay", "genre": "action drama adventure"},
    {"title": "Lagaan", "genre": "drama sports period"},
    {"title": "Zindagi Na Milegi Dobara", "genre": "drama comedy travel friendship"},
    {"title": "Bajrangi Bhaijaan", "genre": "drama comedy action"},
    {"title": "PK", "genre": "comedy drama sci-fi"},
    {"title": "War", "genre": "action thriller"},
    {"title": "Andhadhun", "genre": "thriller crime mystery"},
    {"title": "Gully Boy", "genre": "drama music biography"}
]

def recommend(movie_name):
    movie_name = movie_name.lower()

   
    user_movie = None
    for movie in movies:
        if movie["title"].lower() == movie_name:
            user_movie = movie
            break

    if user_movie == None:
        print("Movie not found. Try these:", [m["title"] for m in movies])
        return

   
    user_genres = user_movie["genre"].split()
    recommendations = []

    for movie in movies:
        if movie["title"].lower() == movie_name: # skip the same movie
            continue

        score = 0
        for genre_word in user_genres:
            if genre_word in movie["genre"]:
                score += 1

        if score > 0: 
            recommendations.append((movie["title"], score))

    
    recommendations.sort(key=lambda x: x[1], reverse=True)

    print(f"\nBecause you liked '{user_movie['title']}', you may also like:")
    if len(recommendations) == 0:
        print("No similar movies found.")
    else:
        for i, (title, score) in enumerate(recommendations[:3], 1): # show top 3
            print(f"{i}. {title}")


print("=== CODSOFT Bollywood Recommender ===")
print("Available movies:", [m["title"] for m in movies])
user_input = input("\nEnter a movie name you like: ")
recommend(user_input)

input("\nPress Enter to exit...")