Q1 = input("What is the capital of France? ")
Q2 = input("What is 2 + 2? ")
Q3 = input("What is the largest mammal? ")
Q4 = input("What is the chemical symbol for water? ")
Q5 = input("Who wrote 'Romeo and Juliet'? ")

def tally_score():
    score = 0
    if Q1.lower() == "paris":
        score += 1
    if Q2 == "4":
        score += 1
    if Q3.lower() == "blue whale":
        score += 1
    if Q4 == "H2O":
        score += 1
    if Q5.lower() == "william shakespeare":
        score += 1
    return score

if Q1.lower() == "paris":
    print("Correct! The capital of France is Paris.")
else:
    print("Incorrect. The correct answer is Paris.")

if Q2 == "4":
    print("Correct! 2 + 2 equals 4.")
else:
    print("Incorrect. The correct answer is 4.")

if Q3.lower() == "blue whale":
    print("Correct! The largest mammal is the blue whale.")
else:
    print("Incorrect. The correct answer is the blue whale.")

if Q4 == "H2O":
    print("Correct! The chemical symbol for water is H2O.")
else:
    print("Incorrect. The correct answer is H2O.")

if Q5.lower() == "william shakespeare":
    print("Correct! 'Romeo and Juliet' was written by William Shakespeare.")
else:
    print("Incorrect. The correct answer is William Shakespeare.")

score = tally_score()
print(f"Your score is {score}/5.")