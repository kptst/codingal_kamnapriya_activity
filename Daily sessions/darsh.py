


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
    
    

# Basics of Image Manipulation
    
import cv2
import matplotlib.pyplot as plt
import numpy as np
import requests

# Load image from URL
url = "https://images.contentstack.io/v3/assets/bltcedd8dbd5891265b/blt5f18c2119ce26485/6668df65db90945e0caf9be6/beautiful-flowers-lotus.jpg?q=70&width=3840&auto=webp"
response = requests.get(url)
image_arr = np.asarray(bytearray(response.content), dtype=np.uint8)
image = cv2.imdecode(image_arr, cv2.IMREAD_COLOR)

# Convert to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title('RGB Image')
plt.axis('off')
plt.show()

# Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.show()



# Image Annotation
import cv2
import matplotlib.pyplot as plt

image_path='example.jpg'
image=cv2.imread(image_path)
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

height,width, _ =image_rgb.shape #get image dimension

# Step2-Draw rect
rect1_width,rect1_height=100,50
top_left1=(20,20)
bottom_right1=(top_left1[0]+rect1_width,top_left1[1]+rect1_height)
cv2.rectangle(image_rgb,top_left1,bottom_right1,(0,255,255), 3)

rect2_width,rect2_height=200,150
top_left2=(width-rect2_width-20,height-rect2_height-20)
bottom_right2=(top_left2[0]+rect2_width,top_left2[1]+rect2_height)
cv2.rectangle(image_rgb,top_left2,bottom_right2,(255,0,255), 3)

center1_x= top_left1[0]+rect1_width//2
center1_y= top_left1[1]+rect1_height//2
center2_x= top_left2[0]+rect2_width//2
center2_y= top_left2[1]+rect2_height//2
cv2.circle(image_rgb,(center1_x,center1_y),5,(0,0,255),-1) #green color filled in circle
cv2.circle(image_rgb,(center2_x,center2_y),5,(0,0,255),-1) #red color filled in circle

cv2.line(image_rgb, (center1_x,center1_y), (center2_x,center2_y), (255,0,0), 3)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb, 'Region 1', (top_left1[0], top_left1[1]-10), font, 0.5, (0, 255, 255), 2, cv2.LINE_AA)
cv2.putText(image_rgb, 'Region 2', (top_left2[0], top_left2[1]-10), font, 0.5, (255, 0, 255), 2,)
cv2.putText(image_rgb, 'Center 1', (center1_x,center1_y-10), font, 0.5, (255, 0, 0), 2, cv2.LINE_AA)
cv2.putText(image_rgb, 'Center 2', (center2_x,center2_y-10), font, 0.5, (255, 0, 0), 2, cv2.LINE_AA)


arrow_start= (width-50, 20)
arrow_end= (width-50, height-20)

cv2.arrowedLine(image_rgb, arrow_start, arrow_end, (0, 255, 0), 3, tipLength=0.05)
cv2.arrowedLine(image_rgb, arrow_end, arrow_start, (0, 255, 0), 3, tipLength=0.05)

height_label_position = (arrow_start[0]-150, (arrow_start[1]+arrow_end[1])//2)
cv2.putText(image_rgb, 'Height', height_label_position, font, 0.5, (0, 255, 0), 2, cv2.LINE_AA)

plt.figure(figsize=(10, 6))
plt.imshow(image_rgb)
plt.title('Image with Annotations')
plt.axis('off')
plt.show()