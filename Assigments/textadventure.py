choice = input("> ")
def start_adventure():
    print("You turn on your console. What account do you login too ")
    print("1. Main account")
    print("2. alt account")
    print("3. secondary alt account")
    print("4. turn off your console and go outside to keep your sanity.")


    if choice == "1":
        main_account()
    elif choice == "2":
        alt_account()
    elif choice == "3":
        secondary_alt_account()
    elif choice == "4":
        leave()
    else:
        print("Invalid choice. Try again.")
        start_adventure()
def main_account():
    print("You put a password on your main...")
    print("1. 8259")
    print("2. 2009")
    print("3. 5209")
    print("4. Give up")


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
        leave()
    else:
        print("Invalid choice. Try again.")
        main_account()
def main_choice():
    print("You've successfully logged in what will you do now?")
    print("1. open youtube.")
    print("2. open tom clancy's rainbow six siege.")
    print("3. decide you have better things to do with your life and get off.")

    if choice == "1":
        print("you opened youtube")
    elif choice == "2":
        print("Internet connection failed please try again later.")
        main_choice()
    elif choice == "3":
        print("You turn off your console.")
        leave()
def alt_account():
    print("You login to your alt account. What do you do next.")
    print("1. ")
    print("2. ")
    print("3. ")
def secondary_alt_account():
    print
def leave():
    print






start_adventure()




