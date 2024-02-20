print("Welcome to Hitman: The Game!")

begin = (input(
    "Your mission is to kill the leader of the group, THE COMPANY! Will you accept this mission? Enter y or n: ")).lower()
if begin == "y":
    print("Welcome to the team!")
    weapon = (input("Before you are three weapons: a gun, a knife, and a stick. Which will you choose for your journey? ")).lower()

    if weapon == "gun":
        print("Very smart choice! You will want all the firepower you can get!")
        location = (input("Okay we know where THE COMPANY is hiding out. How would you like to enter the facility? The roof vent or the front door? "))

        if location == "roof vent" or "vent":
            print("Alright climb that latter over there, and get into the vent")

        elif location == "front door" or "door":
            print("Well if that's what you think is good, go for it!")

        else:
            print("So you aren't going to enter the building then? A helicopter is on route to pick you up. You will be promptly fired after your pickup.")
            print("Game Over")

    elif weapon == "knife":
        print("Alright a knife, we can work with this.")
        location = (input(
            "Okay we know where THE COMPANY is hiding out. How would you like to enter the facility? The roof vent or the front door? "))

        if location == "roof vent" or "vent":
            print("Alright climb that latter over there, and get into the vent")

        elif location == "front door" or "door":
            print("Well if that's what you think is good, go for it!")

        else:
            print(
                "So you aren't going to enter the building then? A helicopter is on route to pick you up. You will be promptly fired after your pickup.")
            print("Game Over")

    elif weapon == "stick":
        print("Wow okay, I guess we will see how far you get.")
        location = (input(
            "Okay we know where THE COMPANY is hiding out. How would you like to enter the facility? The roof vent or the front door? "))

        if location == "roof vent" or "vent":
            print("Alright climb that latter over there, and get into the vent")

        elif location == "front door" or "door":
            print("Well if that's what you think is good, go for it!")

        else:
            print(
                "So you aren't going to enter the building then? A helicopter is on route to pick you up. You will be promptly fired after your pickup.")
            print("Game Over")

    else:
        print("Okay no weapon, best of wishes to you then.")
        location = (input(
            "Okay we know where THE COMPANY is hiding out. How would you like to enter the facility? The roof vent or the front door? "))

        if location == "roof vent" or "vent":
            print("Alright climb that latter over there, and get into the vent")

        elif location == "front door" or "door":
            print("Well if that's what you think is good, go for it!")

        else:
            print(
                "So you aren't going to enter the building then? A helicopter is on route to pick you up. You will be promptly fired after your pickup.")
            print("Game Over")
else:
    print("Your memory is now being wiped. You never met us.")
