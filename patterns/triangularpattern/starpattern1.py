# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# *
# **
# ***
# ****

n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()