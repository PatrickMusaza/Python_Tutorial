print("You are in a haunted house.")
choice = input("Do you want to go left or right? ").lower()

if choice == "left":
    print("You encounter a ghost!")
    action = input("Do you run or fight? ").lower()
    if action == "run":
        print("You escape safely!")
    else:
        print("The ghost scares you away.")
else:
    print("You find a hidden treasure! You win!")
