# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# AAAA
# BBBB
# CCCC
# DDDD

n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        char = chr(ord('A')+i)
        print(char, end="")
    print()