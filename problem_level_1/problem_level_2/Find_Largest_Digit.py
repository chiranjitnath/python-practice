num = int(input("Enter Your Number : "))
check = 0 
while num >= check :
    a = num % 10
    if a > check :
        belief = a
        check = max(check,a)
    num = num // 10

print(f"The Laegest Number Is : {belief}")

