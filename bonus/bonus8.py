date = input("Enter Today's date: ")
mood = input("How you rate your mood today from 1 to 10: ")
thought = input("Let your thought flow:\n ")

with open(f"./journal/{date}.txt", "w") as file:
    file.write(mood + ". ")
    file.write(thought)



