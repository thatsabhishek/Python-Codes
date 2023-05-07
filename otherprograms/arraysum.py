''' Program to add all the elements in an Array.'''

n = int(input("Enter the number of elements: "))
l = []
print("Enter elements: ")
for i in range(n):
    l.append(int(input()))

print("List:",l)
sum = 0
for i in range(n):
    sum += l[i]
    
print("Sum: ",sum)