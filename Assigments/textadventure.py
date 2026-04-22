
def start_adventure():
    print("You turn on your console. What account do you login too ")
    print("1. Main account")
    print("2. alt account")
    print("3. secondary alt account")
    print("4. turn off your console and go outside to keep your sanity.")
    print("5. get off and take a nap.")

    choice = input("> ")

    if choice == "1":
        main_account()
    elif choice == "2":
        alt_account()
    elif choice == "3":
        secondary_alt_account()
    elif choice == "4":
        leave_()
    elif choice == "5":
        print("You get off your console and take a nap.")
        nap()
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
    print("1. look at your messages and notifications.")
    print("2. Watch a movie.")
    print("3. log off and do something else.")

    choice = input("> ")

    if choice == "1":
        print("You look at your messages and notifications.")
        messages()
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
        soccer_position()
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
    print("4. Kwebbelkop")

    choice = input("> ")

    if choice == "1":
        print("You watch Joe Bart and eventually fall asleep.")
    elif choice == "2":
        print("You watch Skittlz and gain motivation to try and play rainbow six siege.")
        main_choice()
    elif choice == "3":
        print("You watch ooziie and decide to play rainbow six siege.")
        main_choice()
    elif choice == "4":
        print("You watch Kwebbelkop.")
        kwebble_Ending()
    else:
        print("Invalid choice. Try again.")
        youtube()

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
        start_adventure()
    elif choice == "4":
        print("You swim for 5 hours and dont make it out of the lake.")
        Ending_Bad()
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
        start_adventure()
    elif choice == "4":
        print("You run for 5 hours and collapse on the ground.")
        Ending_Bad()
    else:
        print("Invalid choice. Try again.")
        Run()

def soccer_position():
    print("What position will you play?")
    print("1. Goalkeeper")
    print("2. Defender")
    print("3. Midfielder")
    print("4. Striker")

    choice = input("> ")

    if choice == "1":
        print("You play goalkeeper and have a great time.")
        soccer_time()
    elif choice == "2":
        print("You play defender and have a great time.")
        soccer_time()
    elif choice == "3":
        print("You play midfielder and have a great time.")
        soccer_time()
    elif choice == "4":
        print("You play striker and have a great time.")
        soccer_time()
    else:
        print("Invalid choice. Try again.")
        soccer_position()

def soccer_time():
    print("How long will you play for?")
    print("1. 30 minutes")
    print("2. 1 hour")
    print("3. 2 hours")
    print("4. 5 hours")

    choice = input("> ")

    if choice == "1":
        print("You play soccer for 30 minutes and collapse from sadness because you're not good at it and didnt play enough.")
        Ending_Bad()
    elif choice == "2":
        print("You play soccer for 1 hour and feel good.")
        Ending_Mid()
        start_adventure()
    elif choice == "3":
        print("You play soccer for 2 hours and feel estatic.")
        Ending_Mid()
    elif choice == "4":
        print("You play soccer for 5 hours and feel fulfilled.")
        Ending_Good()
    else:
        print("Invalid choice. Try again.")
        soccer_time()

def messages():
    print("You have 1 new message and 5 new notifications.")
    print("1. Check the message.")
    print("2. Check the notifications.")
    print("3. Ignore them and do something else.")

    choice = input("> ")

    if choice == "1":
        print("You check the message and its from your friend asking to play.")
        respond = input("Do you want to play with your friend? (yes or no) ")
        if respond.lower() == "yes":
            print("You play with your friend and have a great time.")
    elif choice == "2":
        print("You check the notifications and see that you have a new follower.")
        messages()
    elif choice == "3":
        print("You ignore the message and notifications and do something else.")
        start_adventure()
    else:
        print("Invalid choice. Try again.")
        messages()

def nap():
    print("How long will you nap for?")
    print("1. 30 minutes")
    print("2. 1 hour")
    print("3. 2 hours")
    print("4. 5 hours")

    choice = input("> ")

    if choice == "1":
        print("You nap for 30 minutes and feel refreshed.")
        after_nap = input("Do you want to do something else? (yes or no) ")
        if after_nap.lower() == "yes":
            choice_after_nap()
    elif choice == "2":
        print("You nap for 1 hour and feel accomplished.")
        after_nap = input("Do you want to do something else? (yes or no) ")
        if after_nap.lower() == "yes":
            choice_after_nap()
    elif choice == "3":
        print("You nap for 2 hours and feel very accomplished.")
        after_nap = input("Do you want to do something else? (yes or no) ")
        if after_nap.lower() == "yes":
            choice_after_nap()
        start_adventure()
    elif choice == "4":
        print("You nap for 5 hours and wake up feeling like you wasted your day.")
        bad_nap()
    else:
        print("Invalid choice. Try again.")
        nap()

def choice_after_nap():
    print("What do you want to do after your nap?")
    print("1. Turn on your console and play some games.")
    print("2. Go outside and do something active.")
    print("3. Do something else.")

    choice = input("> ")

    if choice == "1":
        print("You turn on your console and play some games.")
        start_adventure()
    elif choice == "2":
        print("You go outside and do something active.")
        leave_()
    elif choice == "3":
        print("You decide to do something else.")
        start_adventure()
    else:
        print("Invalid choice. Try again.")
        choice_after_nap()

def gaming_store():
    print("You walk into the gaming store and see tons of new games and equipment.")
    print("1. Buy a new game.")
    print("2. Look at gaming headsets.")
    print("3. Check out the trading card section.")
    print("4. Leave the store.")

    choice = input("> ")

    if choice == "1":
        print("You buy a new game and rush home to play it.")
        start_adventure()
    elif choice == "2":
        print("You try on a gaming headset and it sounds amazing. You buy it.")
        Ending_spending()
    elif choice == "3":
        print("You spend hours looking through trading cards and end up spending all your money.")
        Ending_spending()
    elif choice == "4":
        print("You decide not to spend money and leave the store.")
        start_adventure()
    else:
        print("Invalid choice. Try again.")
        gaming_store()

def friend_meetup():
    print("You meet your friend at the mall. What do you want to do?")
    print("1. Go to the arcade.")
    print("2. Grab some food at the food court.")
    print("3. Go see a movie.")
    print("4. Head back home.")

    choice = input("> ")

    if choice == "1":
        print("You play arcade games with your friend all day. It was awesome!")
        Ending_Arcade()
    elif choice == "2":
        print("You and your friend grab some delicious food and chat for hours.")
        Ending_Food()
    elif choice == "3":
        print("You and your friend watch a movie together. Great time!")
        movie_theater()
    elif choice == "4":
        print("You head back home with your friend.")
        start_adventure()
    else:
        print("Invalid choice. Try again.")
        friend_meetup()

def gym_session():
    print("You arrive at the gym and pick your workout.")
    print("1. Hit the weights for an intense session.")
    print("2. Do cardio on the treadmill.")
    print("3. Join a fitness class.")
    print("4. Just use the sauna and relax.")

    choice = input("> ")

    if choice == "1":
        print("You lift heavy weights for 2 hours and feel super strong. You leave feeling pumped!")
        Ending_Gym()
    elif choice == "2":
        print("You run on the treadmill for an hour and feel exhausted but accomplished.")
        Ending_Gym()
    elif choice == "3":
        print("You join a spinning class and push yourself to the limit. You collapse after class.")
        Ending_Bad()
    elif choice == "4":
        print("You relax in the sauna for 30 minutes and feel refreshed.")
        Sauna()
    else:
        print("Invalid choice. Try again.")
        gym_session()

def movie_theater():
    print("You're at the movie theater. What genre do you want to watch?")
    print("1. Action movie.")
    print("2. Horror movie.")
    print("3. Comedy movie.")
    print("4. Leave the theater.")

    choice = input("> ")

    if choice == "1":
        print("You watch an action-packed movie with explosions and fight scenes. It was incredible!")
        Ending_movie()
    elif choice == "2":
        print("You watch a horror movie that scares you so much you can't sleep for days.")
        ending_horror()
    elif choice == "3":
        print("You watch a comedy and laugh the whole time. Great day!")
        Ending_comedy()
    elif choice == "4":
        print("You decide the prices are too high and leave the theater.")
        start_adventure()
    else:
        print("Invalid choice. Try again.")
        movie_theater()

def coffee_shop():
    print("You enter a cozy coffee shop. What will you do?")
    print("1. Order a fancy coffee drink.")
    print("2. Study or work on your laptop.")
    print("3. Meet someone interesting at the coffee shop.")
    print("4. Leave without buying anything.")

    choice = input("> ")

    if choice == "1":
        print("You order a delicious specialty coffee and enjoy every sip.")
        Ending_Coffee()
    elif choice == "2":
        print("You spend 4 hours productively working with amazing coffee. You feel accomplished!")
        Ending_Coffee()
    elif choice == "3":
        print("You meet someone interesting and have a great conversation. Maybe a new friendship!")
        friend_meetup()
    elif choice == "4":
        print("You leave the coffee shop and head elsewhere.")
        start_adventure()
    else:
        print("Invalid choice. Try again.")
        coffee_shop()

def Sauna():
    print("You relax in the sauna for 30 minutes and feel refreshed.")
    after_sauna = input("Do you want to do something else? (yes or no) ")
    if after_sauna.lower() == "yes":
        choice_after_sauna()
    else:
        start_adventure()

def choice_after_sauna():
    print("What do you want to do after the sauna?")
    print("1. Turn on your console and play some games.")
    print("2. Go outside and do something active.")
    print("3. Do something else.")

    choice = input("> ")

    if choice == "1":
        print("You turn on your console and play some games.")
        start_adventure()
    elif choice == "2":
        print("You go outside and do something active.")
        leave_()
    elif choice == "3":
        print("You decide to do something else.")
        start_adventure()
    else:
        print("Invalid choice. Try again.")
        choice_after_sauna()

def bad_nap():
    print("You nap for 5 hours and wake up feeling like you wasted your day.")
    print("You feel bad about yourself and decide to turn on your console to try and make yourself feel better. But you cant log in to any of your accounts because you forgot the passwords. You feel even worse and decide to go outside but you dont have the energy to do anything. You just sit there and feel bad about yourself for the rest of the day.")

def Ending_movie():
    print("You watch an action-packed movie with explosions and fight scenes. It was incredible! You had a great day and feel fulfilled. And gain 10 million dollars. And a good nights rest. You win the game.")

def ending_horror():
    print("You watch a horror movie that scares you so much you can't sleep for days. You feel jittery and anxious. So you decide to go home and do something.")
    start_adventure()

def Ending_comedy():
    print("You watch a comedy and laugh the whole time. Great day! You had a great day and feel fulfilled. And a good nights rest. You win the game.")

def Ending_spending():
    print("You spent all your money on gaming equipment and games. You have no money left to do anything else. You become homeless. You lose the game.")

def Ending_Gym():
    print("You had a great workout and feel amazing. You gain 5 million dollars from your new fitness influencer career. You win the game.")

def Ending_Food():
    print("You and your friend grab some delicious food and chat for hours. You had a great time but you spent all your money on food. You lose the game.")

def Ending_Arcade():
    print("You had a great time playing arcade games with your friend. But you spent all your money on tokens and prizes. You lose the game.")

def Ending_Coffee():
    print("The coffee had too much caffeine and you can't sleep for days. You feel jittery and anxious. And eventually you fall into a permanent sleep. You lose the game.")

def Ending_Good():
    print("You had a great day and feel fulfilled. And gain 10 million dollars. And a good nights rest. You win the game.")

def Ending_Mid():
    print("You had a good day and feel good. And gain a thousand dollars. And a good nights rest.")

def Ending_Bad():
    print("You had a bad day and feel bad. And lose 100 million dollars. You never make it home. You lose the game.")

def kwebble_Ending():
    print("You watch Kwebbelkop. You dislike the video and the AI notices. The AI gets mad. It tracks your ip address and finds you. You must hide. Where will you hide? ")
    print("Closet")
    print("Under the bed")
    print("Behind the shower curtain")
    print("In the attic")
    print("In the basement")

    choice = input("> ")

    if choice.lower() == "closet":
        print("You hide in the closet but the AI finds you and you lose the game.")
    elif choice.lower() == "under the bed":
        print("You hide under the bed but the AI finds you and you lose the game.")
    elif choice.lower() == "behind the shower curtain":
        print("You hide behind the shower curtain. The AI finds you.")
    elif choice.lower() == "in the attic":
        print("You climb into the attic and hide. But the AI grabs you. You're never seen again.")
    elif choice.lower() == "in the basement":
        print("You hide in the basement but the AI finds you. It takes you.")
    else:
        print("Invalid choice. Try again.")
        kwebble_Ending()
    

start_adventure()