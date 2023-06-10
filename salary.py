n = int(input("Enter your Salary: "))

# if( n <= 10000 ):
#     da = 0.105*n
#     ta = 0.105*(n-da)
#     hra = 0.115*(n - ta)
#     pf = 0.135*(n - hra)
#     lic = 0.105*(n - pf)
#     total=da+ta+hra+pf+lic
#     print(lic,"\n", da,"\n",ta,"\n")
#     print(n-total)

if( n <= 10000 ):
    da = 0.105*n
    ta = 0.105*n
    hra = 0.115*n
    pf = 0.135*n
    lic = 0.105*n
    total=da+ta+hra+pf+lic
    print("Daily allowance is: ", da)
    print("TA is: ", ta)
    print("House rent allowance is: ", hra)
    print("Provient Fund is: ", pf)
    print("LIC is: ", lic)
    print("Now your salary is left: ",n-total," from ",n)