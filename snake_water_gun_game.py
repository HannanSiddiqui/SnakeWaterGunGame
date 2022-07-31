import random

def gameWin(comp,Player_choice):
    if comp == Player_choice:
        return None
    elif comp == 's':
        if Player_choice == 'w':
            return False
        elif Player_choice=='g':
            return True
    elif comp == 'w':
        if Player_choice == 'g':
            return False
        elif Player_choice=='s':
            return True
    elif comp == 'g':
        if Player_choice == 's':
            return False
        elif Player_choice == 'w':
            return True

print("Compter choice : Press {s} for snake, Press {w} for water , press {g} for gun : ")
rand_No = random.randint(1,3)
if rand_No == 1:
    comp = 's'
if rand_No == 2:
    comp = 'w'
if rand_No == 3:
    comp = 'g'

Player_choice = input("Player's choice : Press {s} for snake, Press {w} for water , press {g} for gun : ")

print(f'Computer choses {comp}')
print(f'Computer choses {Player_choice}')

Result = gameWin(comp,Player_choice)

if Result== None:
    print("Game Tie!")
elif Result:
    print("you win!")
else:
    print("You lose!")