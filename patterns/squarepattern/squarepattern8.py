# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# DCBA
# DCBA
# DCBA
# DCBA

n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        char = chr(ord('A')+n-j)
        print(char, end="")
    print()