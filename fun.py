
## Introduces the game: 3am
print("------ 3 am -------")




def shadowy_figure():
    print("You walk up to the shadowy figure.")
    print("He has no face.")
    print("He hands you a business card with his name on it: Mr. Beautiful.")
    print("You read the card, \"I make people disappear.\"")
    print("")

    while True:
        print("You have a choice.")
        print("- Punch.")
        print("- Run.")



        move4 = input("> ")

        if move4 == "punch":
            dead("You throw a jab, cross, lead-hook, uppercut combo, and Mr. Beautiful runs away crying.")
        elif "run":
            dead("You run away and go back into your apartment.")
        else:
            print("You have to do something.")


# create a function for going outside
def outside_1():
    print("You are now outside. It's a little chilly, but not too bad.")
    print("You look down the stairs. Not a lot going on at 3am.")
    print("You close the door behind you and walk down the stairs. You are now facing West.")

    # This block of code will hold true when the user steps outside.
    while True:
        print("The air around you is foggy. Visibility is pretty low.")
        print("You can see the fog-hazed yellowish glow of the lamp post on your corner to the South.")
        print("A shadowy figure stands below the lamp post.")

        # input commands for outside in the foggy night
        move3 = input("> ")

        if move3 == "north":
            print("To your north there is a dumpster. It smells pretty nasty. Screw that.")
            print("")

        if move3 == "south":
            print("You walk toward the shadowy figure.")
            print("")
            shadowy_figure()


        if move3 == "east":
            print("You don't want to go back up the stairs right now.")
            print("")

        if move3 == "west":
            print("Your car is parked in its space under the carport.")
            print("")



# creates a function for the user walking to the front door.
def front_door():
    print("You are at the front door. The door is open and you can feel the breeze.")
    print("You can hear the sound of cars passing and sirens in the distance. City life.")
    print("")

    # This block of code holds true while user is at front door.
    while True:
        print("You enjoy the cool breeze coming in through the front door.")
        print("You wonder why you're alone. Someone was here earlier.")
        print("To the north are the stairs.")
        print("To the south, east and west is the interior of your apartment.")
        print("")

        # if user moves while at front door, accept following input
        move2 = input("> ")

        # if user goes north, they will be taken to another function called outside_1
        if move2 == "north":
            outside_1()

        # if user types anything other than north, they are told they don't really have a choice.
        else:
            print("No. You're going outside.")
            print("")




# Create a function for getting out of bed.
def got_up():
    print("""You feel around for your shoes, and put them on.""")
    print("")

    # create possible moves for the user after they get out of bed.
    while True:
        print("To the north is your front door.")
        print("To the south is your bed.")
        print("To the east is your bedroom window.")
        print("To the west is your closet.")
        print("")

        move1 = input("> ")

        if move1 == "north":
            front_door()

        elif move1 == "south":
            print("You just woke up. You're not going back to bed.")
            print("")

        elif move1 == "east":
            print("Out the window you can see the parking lot. Your car is still there.")
            print("")

        elif move1 == "west":
            print("There is nothing but clothes over there.")
            print("")




# create a function for dead
def dead(why):
    print(why, "Game over. You win.")
    exit(0)

# Game start function, which is called below this block of code.
def start():
    print("")
    print("""The front door is wide open. The apartment is cold.
You look at the alarm clock and it's 3:00am.\n Get up? \n Go back to sleep? """)
    print("")

    # Give the illusion of choice.
    choice = input("> ")

    if choice == "Get up":
        print("""You crawl out of bed as you look around the room. It's pitch black, but there are no Grues in this game.""")
        print("")
        got_up()
    elif choice == "Go back to sleep":
        print("You attempt to sleep, but the room is too cold. There's an eerie silence.")
        print("")
        start()
    else:
        print("You don't have much of a choice. Perhaps you should get up.")
        print("")
        got_up()

# game starts
start()
