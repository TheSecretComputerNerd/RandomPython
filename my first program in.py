print("Hello world")
choice = input("hey buddy, how is it going, good, bad, ugly or oogly?").upper()
if choice == "GOOD":
    print("That's great to hear!")
elif choice == "BAD":
    print("Why not have tea to cheer up!")
elif choice == "UGLY":
    print("wow. you are having a bad day. Get a life.")
elif choice == "OOGLY":
    print("I don't even Know what that means! Is it fun?")
elif choice == "NO":
    print("Okay bye")
else: print("Okay great!")
choice = input("anything else you want to (no, good, bad, ughly or oogly?)").upper()
