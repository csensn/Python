n = int(input("Enter a number: "))

# ================= PERFECT NUMBER =======================
# sum=0
# for i in range(1,n):
#     if(i%2==0):
#         sum=sum+i
# if sum = n:
#     print("Perfect")
# else:
#     print("Not perfect")
# ==============================================================


# ================== PRIME NUMBER ==============================
# count = 0
# for i in range(1,n+1):
#     if(n%i==0):
#         count=count+1
# if(count==2):
#     print(f"{n} is a prime number.")
# else:
#     print(f"{n} is not prime number.")

# =================== PRIME NUMBER SECOND METHOD ======================

# sum =0
# for i in range(1,n+1):
#     if(n%i==0):
#         sum = sum + i
# if(sum == n+1):
#     print(f"{n} is a prime number.")
# else:
#     print(f"{n} is not prime number.")
# =======================================================================

# ==================== FACTORIAL ===================================
# from math import factorial
#
# print(factorial(n))
#
# fact =1
# for i in range(n, 0, -1):
#     fact = fact*i
#     print(i, end="*")
# print("\b =", fact)
#
# ====================================================================

sum =0

for i in range(10):
    num = int(input("Enter a number : "))
    if (num % 2 == 0):
        sum = sum + num
        # print("Sum: ", sum)
    else:
        print("Not added.")

print("Sum: ",sum)
# =============================
# import pyttsx3
# friends = ["Maamu", "Deevrshi ", "Girdhari ","Dalpat ","Vikram "]
#
# for i in range(0, len(friends)):
#     print(friends)
#
# i=1
# for data in friends:
#     print(f"Your {i} firend is : {data}")
#     pyttsx3.speak(f"Your {i} friend is : {data}")
#     i+=1
# ====================================================

# ============== WHILE LOOP ===========================

i=1
while(i<10):
    print(i)
    i+=1