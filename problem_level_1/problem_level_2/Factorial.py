n = int(input("Enter Your Number : "))
result = 1
if n == 1 or n == 0 :
    print(f"Factorial is : {result}")

else :
    for i in range (1,n+1):
        result = result * i
    

    print (f"Factorial is : {result}")