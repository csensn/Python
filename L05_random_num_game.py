from random import *

n = randint(1,100)
number_of_gusses = 0
print("Number of success is limited only 10 times.")

while(number_of_gusses <=10):
    g_anumber = int(input("Enter a numner: "))
    if(g_anumber > n):
        print("Number is grater enter a small number...")
    elif(g_anumber < n):
        print("Number is low enter a grater number....")
    else:
        print("You won.......!")
        print(number_of_gusses, "no. of guesses you win.")
        break
    print(9 - number_of_gusses, "is left.")
    number_of_gusses = number_of_gusses + 1
if(number_of_gusses == 10):
    print("Game over.....?")