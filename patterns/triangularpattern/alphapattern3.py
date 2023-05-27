# Print the following pattern for the given N number of rows.
# Pattern for N = 4
#    A
#   BCD
#  EFGHI
# JKLMNOP

n = int(input("Enter the number of rows: "))
for i in range(1, n+1): 
    for sp in range(n-i):
        print(" ", end="")
    for j in range(i):
        print(chr(ord('A') + i + j - 1), end="")
    for k in range(i-1):
        print(chr(ord('A') + i + j - k), end="")
    print()