print("AI Recommendation System")

user_input = input("What do you like? (movies/food/study): ")

if user_input == "movies":
    print("Avengers, Interstellar, John Wick")
elif user_input == "food":
    print("Nasi Lemak, Ramen, Chicken Rice")
elif user_input == "study":
    print("Python, Math, AI Basics")
else:
    print("No recommendation")
