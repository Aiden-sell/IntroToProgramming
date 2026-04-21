
def start_adventure():
    print("You turn on your console. What account do you login too ")
    print("1. Main account")
    print("2. alt account")
    print("3. secondary alt account")
    print("4. turn off your console and go outside to keep your sanity.")

    choice = input("> ")

    if choice == "1":
        main_account()
    elif choice == "2":
        alt_account()
    elif choice == "3":
        secondary_alt_account()
    elif choice == "4":
        leave_()
    else:
        print("Invalid choice. Try again.")
        start_adventure()
        
        
def main_account():
    print("You put a password on your main...")
    print("1. 8259")
    print("2. 2009")
    print("3. 5209")
    print("4. Give up")

    choice = input("> ")

    if choice == "1":
        print("incorrect try again.")
        main_account()
    elif choice == "2":
        print("incorrect try again.")
        main_account()
    elif choice == "3":
        print("you succussfully logged in.")
        main_choice()
    elif choice == "4":
        print("You give up on getting into your main account")
        leave_()
    else:
        print("Invalid choice. Try again.")
        main_account()
def main_choice():
    print("You've successfully logged in what will you do now?")
    print("1. open youtube.")
    print("2. open tom clancy's rainbow six siege.")
    print("3. decide you have better things to do with your life and get off.")

    choice = input("> ")

    if choice == "1":
        print("you opened youtube")
        youtube()
    elif choice == "2":
        print("Connection failed please try again later.")
        main_choice()
    elif choice == "3":
        print("You turn off your console.")
        leave_()
    else:
        print("Invalid choice. Try again.")
        main_choice()

def alt_account():
    print("You login to your alt account. What do you do next.")
    print("1. open tom clancy's rainbow six siege.")
    print("2. Play rocket league.")
    print("3. Watch amazon prime.")

    choice = input("> ")

    if choice == "1":
        print("Connection failed please try again later")
        alt_account()
    elif choice == "2":
        print("Connection to epic games severs failed please try again in a minute.")
        alt_account()
    elif choice == "3":
        print("You log onto amazon prime video.")
        amazon_prime()
    else:
        print("Invalid choice. Try again.")
        alt_account()
def secondary_alt_account():
    print("You login to your secondary alt account. What do you do next.")
    print("1. Play a game.")
    print("2. Watch a movie.")
    print("3. Go back.")

    choice = input("> ")

    if choice == "1":
        print("You start playing a game.")
        main_choice()
    elif choice == "2":
        print("You watch a movie.")
        amazon_prime()
    elif choice == "3":
        start_adventure()
    else:
        print("Invalid choice. Try again.")
        secondary_alt_account()

def leave_():
    print("You leave your house and go outside what will you do?")
    print("1. go to a lake and swim. ")
    print("2. Go for a run. ")
    print("3. Play soccer. ")
    print("4. Realize youre not built like that and go back inside. ")

    choice = input("> ")
    if choice == "1":
        print("You go to a lake and swim for the rest of the day. ")
        swim()
    elif choice == "2":
        print("You go for a run and then go home and sleep.")
        Run()
    elif choice == "3":
        print("you go play soccer and have a great day.")
        soccer()
    elif choice == "4":
        print("You walk back into your house and turn your console back on.")
        start_adventure()
    else:
        print("Invalid choice. Try again.")
        leave_()

def youtube():
    print("What will you watch?")
    print("1. Joe Bart")
    print("2. Skittlz")
    print("3. ooziie")

    choice = input("> ")

    if choice == "1":
        print("You watch Joe Bart and eventually fall asleep.")
    elif choice == "2":
        print("You watch Skittlz and gain motivation to try and play rainbow six siege.")
        main_choice()
    elif choice == "3":
        print("You watch ooziie and decide to play rainbow six siege.")
        main_choice()

def amazon_prime():
    print("What will you watch?")
    print("1. The Boys")
    print("2. Invincible")
    print("3. watch something else")
    choice = input("> ")

    if choice == "1":
        print("You watch The Boys and have a great time.")
    elif choice == "2":
        print("You watch Invincible and have a great time.")
    elif choice == "3":
        print("You decide to do something else.")
        start_adventure()
    else:
        print("Invalid choice. Try again.")
        amazon_prime()

def swim():
    print("How long will you swim for?")
    print("1. 30 minutes")
    print("2. 1 hour")
    print("3. 2 hours")
    print("4. 5 hours")

    choice = input("> ")

    if choice == "1":
        print("You swim for 30 minutes and feel refreshed.")
        start_adventure()
    elif choice == "2":
        print("You swim for 1 hour and feel accomplished.")
        start_adventure()
    elif choice == "3":
        print("You swim for 2 hours and feel very accomplished.")
    elif choice == "4":
        print("You swim for 5 hours and dont make it out of the lake.")
    else:
        print("Invalid choice. Try again.")
        swim()

def Run():
    print("How long will you run for?")
    print("1. 30 minutes")
    print("2. 1 hour")
    print("3. 2 hours")
    print("4. 5 hours")

    choice = input("> ")

    if choice == "1":
        print("You run for 30 minutes and feel refreshed.")
        start_adventure()
    elif choice == "2":
        print("You run for 1 hour and feel accomplished.")
        start_adventure()
    elif choice == "3":
        print("You run for 2 hours and feel very accomplished.")
    elif choice == "4":
        print("You run for 5 hours and collapse on the ground.")
    else:
        print("Invalid choice. Try again.")
        Run()

def soccer():
    print("How long will you play soccer for?")
    print("1. 30 minutes")
    print("2. 1 hour")
    print("3. 2 hours")
    print("4. 5 hours")

    choice = input("> ")

    if choice == "1":
        print("You play soccer for 30 minutes and collapse from sadness because you're not good at it and didnt play enough.")
        start_adventure()
    elif choice == "2":
        print("You play soccer for 1 hour and feel good.")
        start_adventure()
    elif choice == "3":
        print("You play soccer for 2 hours and feel estatic.")
    elif choice == "4":
        print("You play soccer for 5 hours and feel fulfilled.")
    else:
        print("Invalid choice. Try again.")
        soccer()




start_adventure()


