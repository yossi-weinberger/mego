# def print_even(n):
#     if n == 0:
#         return
#
#     x = int(input())
#     if x % 2 == 0:
#         print(x)
#     print_even(n - 1)
#
#
# number = int(input("Enter a number: "))
# print_even(number)


def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n -1) + fibo(n - 2)


n = int(input("Enter a number: "))
# fibo(n)
print(fibo(n))