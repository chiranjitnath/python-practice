number = int(input("Enter Your Number : "))
lst = list(map(int,str(number)))
last = []
for i in lst:
    last = [i] + last

reverse = int(''.join(map(str,last)))
print(f"The Reversed Number Is : {reverse}")

