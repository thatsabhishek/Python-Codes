n = int(input("Enter a number: "))
check = 0
for i in range(2,n):
    if n%i == 0:
        check+=1
    else:
        continue
if check == 0:
    print(n,'is a prime number.')
else:
    print(n,'is not a prime number.')