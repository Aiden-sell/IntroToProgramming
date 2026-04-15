import random 

q1 = input("what is your name? ")
q2 = input("what is your lucky number? ")
q3 = input("how many years in the future do you want to see? ")

print(f"Hello {q1}, your lucky number is {q2} and you want to see {q3} years into the future.")
def fortune_teller():
    fortunes = [
        "You will have a great day!",
        "A surprise is waiting for you around the corner.",
        "You will achieve your goals soon.",
        "Happiness is coming your way.",
        "You will meet someone special today.",
        "You will hit SSL in the next " + q3 + " years.",
        "You will tear your ACL in the next " + q3 + " years.",
        "Youre going to stub your toe in " + q3 + " years.",
        "youll get shin splints soon. very soon",
        "you will find a penny in " + q3 + " years.",
        "you will find a nickel in " + q3 + " years.",
        "you will find a dime in " + q3 + " years.",
        "you will find a quarter in " + q3 + " years.",
        "You will might never hit SSL.",
        "your world will end in " + q3 + " years.",
        "you will have a great day in " + q3 + " years.",
        "you will win the lottery in " + q3 + " years.",

    ]
    
    return random.choice(fortunes),

fortune, = fortune_teller()
print(f"Your fortune is: {fortune}")