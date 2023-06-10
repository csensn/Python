# import pyttsx3
#
# n = input("Enter any number: ")[-1]
# n1 = int(input("Enter any number: "))
#
# if((n//2)*2==n):
#     print("Number is Even")
#     pyttsx3.speak("Number is Even.")
# else:
#     print("Number is Odd")
#     pyttsx3.speak("Number is Odd")
# =====================================================
#
# if(n in '0,2,4,6,8'): print("Number is Even")
# =======================================================
#
# if(n in '0,2,4,6,8'):
#     print("Number is Even")
# else:
#    print("Number is Odd")
#
# =========================================================
#
# print("Number is Even") if(n in '0,2,4,6,8') else print("Number is Odd")
#
# ===========================================================
#
# print("You are pass") if(n1 >= 65) else print("Try next time....")
#
# =============================================================
#
# a,b,c = eval(input("Enter three number: "))
#
# if(a>b and a>c):
#     print("a is gratest.")
# elif(b>a and b>c):
#     print("b is gratest.")
# else:
#     print("c is gratest.")
#
# exp = input("Enter the experation: ")
# if('45*3' in exp):
#     print("555")
# elif('66+7' in exp):
#     print("77")
# else:
#     print(eval(exp))
# ===============================================

# n = input("Enter a Alphabet: ")[0]
#
# print(n)
# if(n.lower() in 'a,e,i,o,u'):
#     print("Vowel")
# else:
#     print("Consonent")
# =======================================================

nation = input("Enter the Nationality: ")

if(nation.lower() == "indian"):
    age = int(input("Enter the age: "))
    if(age >= 18):
        print("You are eligible for PAN card.")
    else:
        print("You are not eligible due to age")
else:
    print("You are not eligible du e to nationality")