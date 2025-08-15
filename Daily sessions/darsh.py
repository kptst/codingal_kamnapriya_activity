


# AI MOVIE RECOMENDATION SYSTEM

import random
import time
from textblob import TextBlob

# Sample movie database (can be extended or replaced with a real dataset)
movies = {
    "comedy": [
        {"title": "The Grand Budapest Hotel", "rating": 8.1},
        {"title": "Superbad", "rating": 7.6},
        {"title": "The Hangover", "rating": 7.7}
    ],
    "drama": [
        {"title": "The Shawshank Redemption", "rating": 9.3},
        {"title": "Forrest Gump", "rating": 8.8},
        {"title": "The Godfather", "rating": 9.2}
    ],
    "sci-fi": [
        {"title": "Inception", "rating": 8.8},
        {"title": "Interstellar", "rating": 8.6},
        {"title": "The Matrix", "rating": 8.7}
    ],
    "action": [
        {"title": "Mad Max: Fury Road", "rating": 8.1},
        {"title": "Gladiator", "rating": 8.5},
        {"title": "John Wick", "rating": 7.4}
    ],
    "romance": [
        {"title": "The Notebook", "rating": 7.8},
        {"title": "Pride & Prejudice", "rating": 7.8},
        {"title": "La La Land", "rating": 8.0}
    ]
}

# Display genres
def show_genres():
    print("\nAvailable genres:")
    for i, genre in enumerate(movies.keys(), 1):
        print(f"{i}. {genre.capitalize()}")

# Get genre from user
def get_genre():
    while True:
        show_genres()
        choice = input("\nChoose a genre by name or number: ").strip().lower()
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(movies):
                return list(movies.keys())[index]
        elif choice in movies:
            return choice
        print("Invalid input. Please try again.")

# Analyze mood
def analyze_mood():
    mood = input("\nHow are you feeling today? ").strip()
    polarity = TextBlob(mood).sentiment.polarity
    if polarity > 0.3:
        return "positive"
    elif polarity < -0.3:
        return "negative"
    else:
        return "neutral"

# Get IMDb rating filter
def get_rating():
    try:
        rating = input("\nEnter a minimum IMDb rating (or press enter to skip): ").strip()
        return float(rating) if rating else 0.0
    except ValueError:
        print("Invalid rating. Skipping rating filter.")
        return 0.0

# Simulate processing
def show_processing():
    print("\nProcessing your preferences", end="")
    for _ in range(3):
        time.sleep(0.7)
        print(".", end="", flush=True)
    print()

# Recommend movies
def recommend_movies(genre, mood, min_rating):
    print(f"\n🎬 Recommendations in '{genre.capitalize()}' genre for your {mood} mood:")
    filtered = [m for m in movies[genre] if m["rating"] >= min_rating]
    if not filtered:
        print("No movies found with your selected criteria.")
    else:
        for movie in filtered:
            print(f"- {movie['title']} (IMDb: {movie['rating']})")

# Main system function
def main():
    print("🎉 Welcome to the Personalized Movie Recommender! 🎉")
    name = input("What's your name? ").strip()
    print(f"Hello, {name}! Let's find a great movie for you.")

    while True:
        genre = get_genre()
        mood = analyze_mood()
        min_rating = get_rating()

        show_processing()
        recommend_movies(genre, mood, min_rating)

        again = input("\nWould you like another recommendation? (yes/no): ").strip().lower()
        if again != "yes":
            print("🎬 Thank you for using the Movie Recommender. Happy watching!")
            break

# Run the system
if __name__ == "__main__":
    main()