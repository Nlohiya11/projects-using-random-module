import random

rock = '''(ROCK)

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
paper = '''(PAPER)

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________) '''

scissors = '''(SCISSORS)

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
is_true = True


def cases():
    if choice == 1 and computer_turn == 2:
        print('\nYou Won')
        win = 1
    elif choice == 2 and computer_turn == 0:
        print('\nYou Won')
        win = 1
    elif choice == 3 and computer_turn == 1:
        print('\nYou Won')
        win = 1
    if choice - 1 == computer_turn:
        print("\nIts a Draw")
        win = 0
    else:
        print("\nYou Lost")
        win = -1
    if win == 1:
        print('''\n██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝''')
    elif win == 0:
        print('''\n██████╗ ██████╗  █████╗ ██╗    ██╗
██╔══██╗██╔══██╗██╔══██╗██║    ██║
██║  ██║██████╔╝███████║██║ █╗ ██║
██║  ██║██╔══██╗██╔══██║██║███╗██║
██████╔╝██║  ██║██║  ██║╚███╔███╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ''')
    else:
        print(''' ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝ ''')


while is_true:
    choice = int(input("Choose your move\n Press 1 for rock , Press 2 for paper , press 3 for scissor :\n"))
    computer = random.randint(0, 2)
    if 1 <= choice <= 3:
        if choice == 1:
            print(f"You choose : \n{rock}")
        elif choice == 2:
            print(f"You choose : \n{paper}")
        elif choice == 3:
            print(f"You choose : \n{scissors}")
        computer_turn = computer
        if computer_turn == 0:
            print(f"\ncomputer choose : \n{rock}")
        elif computer_turn == 1:
            print(f"\ncomputer choose : \n{paper}")
        else:
            print(f"\ncomputer choose : \n{scissors}")
        cases()

    else:
        print("")
    if input("\nDo you want to play again? y/n : ") == "y":
        is_true = True
    else:
        is_true = False
