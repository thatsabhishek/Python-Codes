# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 4444
# 4444
# 4444
# 4444

n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        print(n, end="")
    print()