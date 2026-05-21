text = input("Enter a sentence: ").lower()

if "good" in text or "happy" in text or "love" in text:
    print("Positive sentiment")
elif "bad" in text or "sad" in text or "hate" in text:
    print("Negative sentiment")
else:
    print("Neutral sentiment")
