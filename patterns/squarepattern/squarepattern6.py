# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# ABCD
# ABCD
# ABCD
# ABCD

n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        char = chr(ord('A')+j)
        print(char, end="")
    print()