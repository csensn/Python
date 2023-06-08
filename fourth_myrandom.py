from random import *

# print(randint(1,1000))
# print(random())

# frinds = ["Vikram", "Maamu", "Girdhari", "Dalpat"]
# print(choice(frinds))
# ===================================================

# Generate OTP

n = int(input("Enter How much digit OTP: "))

print(randint(10**(n-1),(10**n)-1))