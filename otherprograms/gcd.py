num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
gcd = 1
i = 1

while i<=num1 and i<=num2:
    if num1%i==0 and num2%i==0:
        gcd = i
    i = i+1
print("GCD of",num1,"and",num2,"is",gcd)