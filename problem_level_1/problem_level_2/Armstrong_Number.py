num = int(input("Enter Your Number : "))
temp = num 
og = num
count = 0
total = 0
while temp > 0 :
    temp = temp // 10 
    count += 1 
   
temp = num

while temp > 0 :
    a = temp % 10 
    total += a**count
    temp = temp // 10



if og == total :
    print("This is an Armstrong Number")

else :
    print("This is Not an armstrong Number")
