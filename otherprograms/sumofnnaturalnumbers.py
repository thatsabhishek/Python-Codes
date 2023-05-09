"""
Program for printing the sum of first n natural numbers
"""

n = int(input("Enter n: "))
sum = 0
i = 1
while i<=n:
    sum = sum+i
    i=i+1

print(f"Sum of first {n} numbers is {sum}")

