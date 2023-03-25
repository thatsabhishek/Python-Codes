"""
Armstrong's numbers are those numbers in which cube of each digit in the number ads unto the total number
e.g. 153 = 1 x 1 x 1 + 5 x 5 x 5 + 3 x 3 x 3 = 153,
Hence 153 is an armstrong number.
"""


def is_armstrong_number(num):
    n = num
    a = len(str(n))
    sum_of_digits = 0
    while n > 0:
        x = n % 10
        sum_of_digits += x**a
        n = int(n / 10)
    if sum_of_digits == num:
        return True
    else:
        return False


number = int(input("Enter a number: "))
armstrong_num = is_armstrong_number(number)
if armstrong_num:
    print(f"Yes, number {number} is an armstrong number.")
else:
    print(f"No, number {number} is not an armstrong number.")
