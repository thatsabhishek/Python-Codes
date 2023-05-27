# Print the following pattern for the given N number of rows.
# Pattern for N = 4
#    1
#   232
#  34543
# 4567654

n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
    for sp in range(n-i):
        print(" ", end="")
    for j in range(i):
        print(i+j, end="")
    for k in range(i-1, 0, -1):
        print(k+i-1, end="")
    print()