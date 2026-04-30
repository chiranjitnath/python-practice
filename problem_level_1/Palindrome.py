Num = int(input("Enter Your Number : "))
lst = list(map(int,str(Num)))
Check = []
for i in lst :
    Check = [i] + Check

if lst == Check :
    print("The Number Is a Palindrome")

else :
    print("The Number Is Not a Palindrome")