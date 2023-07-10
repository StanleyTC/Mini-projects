print("""
         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
      
""")
print("Welcome to treasure island! your mission is to find the treasure.")
path = input(("you are at a cross road. Where do you want to go? type 'left' or 'right': ")).lower()
if path != 'left':
    print('You fall into a hole. Game Over')
else:
    lake= input(("you come to a lake. There is a island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swin' to swin across: ")).lower()
    if lake != "wait":
        print("You were attacked by trout. Game over")
    else:
        door = input("you waited and a boat had helped you. Now you are in front of three doors, one red and another blue, what to do? type 'red' to go to the red one, 'yello' to the yellow one, or 'blue' to go to the blue one: ")
        if door != "red" and door != "yellow":
            print('You choose the blue door, there had bests... they eat you, you are dead. Game Over')
        elif door == "yellow":
            print('You found the treasure, congrats!')
        else:
            print("You choose the red one. A fireball was thrown at you, you are dead. Game over!")