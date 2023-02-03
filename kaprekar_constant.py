def Kaprekar_Constant(n):
    square = n**2
    square_str = str(square)
    length = len(str(n))
    for i in range(1, len(square_str)):
        left = int(square_str[:i])
        right = int(square_str[i:])
        if right != 0 and left + right == n:
            return True
    return False

def find_Kaprekar_Numbers(start, end):
    Kaprekar_Numbers = []
    for i in range(start, end + 1):
        if Kaprekar_Constant(i):
            Kaprekar_Numbers.append(i)
    return Kaprekar_Numbers

# example usage
start = 1
end = 10000
print(find_Kaprekar_Numbers(start, end))
