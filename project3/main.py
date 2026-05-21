user = input("Ask me something: ").lower()

if "hello" in user:
    print("Hi there!")
if "how are you" in user:
    print("I am fine, thank you, and you?")
elif "name" in user:
    print("I am a simple AI bot")
else:
    print("Sorry, I don't understand")
