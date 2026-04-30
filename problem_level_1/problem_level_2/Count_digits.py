Num = int(input("Enter Your Number : "))
count = 0 
while Num:
    n = Num % 10 
    Num = Num // 10
    count += 1

print(f"Total Number of Digits are : {count}")
