print("Hello Welcome to mini KBC")
playing = input("Do you want continue with mini KBC? ")
if playing != "Yes":
    quit()
else:
    print("OK! Lets play the game")
    score = 0
    q1 = input("What is the solid form of water? ").strip().lower()
    if q1 == "ice":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    q2 = input("Which organ pumps blood? ")
    if q2 == "heart":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    q3 = input("Which animal is known as the \"Ship of the Desert\"? ")
    if q3 == "camel":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    q4 = input("What is the hardest natural substance on Earth? ")
    if q4 == "diamond":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    q5 = input("Which planet is known as the \"Red Planet\"? ")
    if q5 == "mars":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    q6 = input(" How many days are in a leap year? ")
    if q6 == "366":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    q7 = input("Which city is called the \"City of Joy\"? ")
    if q7 == "kolkata":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    q8 = input("Who is known as the \"Father of the Nation\" in India? ")
    if q8 == "gandhi":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    q9 = input("Which month comes after June? ")
    if q9 == "july":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    q10 = input(" What is the national fruit of India? ")
    if q10 == "mango":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print(f"{score} Correct and {10 - score} incorrect")