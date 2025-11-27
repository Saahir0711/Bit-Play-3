num1 = int(input("Enter your number: "))

def consecutive1s(num1):
    length = 0
    while num1 != 0:
        num1 = num1 & (num1 << 1)
        length += 1
    return length

print ("Longest consecutive 1s length : ", consecutive1s(num1))
