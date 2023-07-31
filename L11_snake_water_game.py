import random

lst = ['s','w','g']
chance = 10
no_of_chance = 0
computer_pont = 0
user_pont = 0

while no_of_chance < chance:
    enter = input(f"Select one: {lst}: ")
    r = random.choice(lst)

    if enter == r:
        print("Tie both have no points")
    elif enter=='s' and r == 'w':
        print("User win and computer loss")
        user_pont+=1
        print(f"User get point {user_pont}")
    elif enter=='s' and r=='g':
        print("User loss and computer win")
        computer_pont+=1
        print(f"Computer get point {computer_pont}")

    elif enter=='w' and r == 's':
        print("User loss and computer win")
        computer_pont+=1
        print(f"Computer get point {computer_pont}")
    elif enter=='w' and r == 'g':
        print("User win and computer loss")
        user_pont+=1
        print(f"User get point {user_pont}")

    elif enter=='g' and r == 'w':
        print("User loss and computer win")
        computer_pont+=1
        print(f"Computer get point {computer_pont}")
    elif enter=='g' and r == 's':
        print("User win and computer loss")
        user_pont+=1
        print(f"User get point {user_pont}")
    no_of_chance+=1
    print(f"{chance - no_of_chance} chances left")

if user_pont > computer_pont:
    print(f"You win the game with the {user_pont} points and computer loss with {computer_pont} points")
elif user_pont < computer_pont:
    print(f"Computer win the game with the {computer_pont} points and you loss with {user_pont} points")
else:
    print(f"Game is Tie you both have same points both have same {computer_pont} points")
print("........Game Over.......")