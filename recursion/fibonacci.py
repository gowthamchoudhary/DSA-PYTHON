# def fibonacci(n):
#     if n==0 or n==1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# num = input("enter a number :")
# print(fibonacci(int(num))) 
input_number = int(input("Enter a number: "))
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a