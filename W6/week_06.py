def start_village():
    print("i was called")
    selected_npc = input("Welcome to the wood village. It's a great idea to get to know the natives, also, they might have some work for you. Who do you want to meet first? (fishman/blacksmith) ").lower()

    if selected_npc == "fishman":
        fish_caught = fishman()
        if fish_caught > 0:
            print(f"Great, you got {fish_caught} fish, you earned {fish_caught * 7}.")
        else:
            print("Fishing is not for everyone.")

    if selected_npc == "blacksmith":
        niobium_caught = blacksmith()

        if niobium_caught > 0:
            print(f"{niobium_caught} pounds of niobium, that's pretty good. You deserve these {niobium_caught * 33} coins.")
        else:
            print("I hope you at least enjoyed the trip!")


def fishman():
    fish_caught = 0
    accept_mission = input("[Fishman] Nice day for fishing ain't it? hu ha! (yes/no) ").lower() == "yes"

    if accept_mission:
        print("The golden lake is the best place for fishing. I pay 2 coins for each fish caught.")
        print("You're in the golden lake!")

        action = ""

        while "back" not in action:
            action = input("What do you want to do? (fish/go back) ").lower()
            if action == "fish":
                fish_caught += 1
                print("Great you got one!")

            if "back" in action:
                print("Let's bring these fish back.")

    else:
        print("All right see you then.")

    return fish_caught


def blacksmith():
    niobium_caught = 0
    accept_mission = input("[Blacksmith] I haven't had so much work since the Erechim War. Are you looking for some work? (yes/no) ").lower() == "yes"

    if accept_mission:
        print("Great, there's a special material named niobium, bring me some.")
        print("Welcome to the dark mine. People might get rich or loose you mind here. Good luck")

        action = ""

        while "back" not in action:
            action = input("What do want to do? (pick/go back) ").lower()
            if "pick" in action:
                niobium_caught += 1
                print("You got some niobium nugget")

            if "back" in action:
                print("I'm surprised! At least you're back alive. Let's see if you've got something. ")

    else:
        print("Tha'ts what I thought. Not everyone is brave enough to work in the dark mine. You're more of a fishman, hu?")

    return niobium_caught


is_new_player = input("You're new here, right? (yes/no) ").lower() == "yes"

if is_new_player:
    print("Welcome. As you've seen, to play this game you'll have to type the according to suggestions.")
else:
    print("Great, have a good game.")

start_village()
