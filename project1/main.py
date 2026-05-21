print("AI Recommendation System")

user_input = input("What do you like? (movies/food/dessert/hobby/novel/study): ")

if user_input == "movies":
    print("The Shawshank Redemption, Big Fish, The Truman Show, Dream of the Red Chamber")
elif user_input == "food":
    print("Wanton Mee, Roti Canai, Satay, Char Kway Teow, Laksa, Bak Kut Teh")
elif user_input == "dessert":
    print("Tofu pudding, Chocolate cake, Tiramisu, Cannoli")
elif user_input == "hobby":
    print("reading novel, listening music, playing badminton, practicing calligraphy")
elif user_input == "novel":
    print("The Vegetarian, To Live, Brothers")
elif user_input == "study":
    print("Python, AddMath, English, AI Basics")
else:
    print("No recommendation")
