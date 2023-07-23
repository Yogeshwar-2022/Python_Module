
# n = 10
# product = 1
# for i in range(n):
#     product = product*(i+1)
# print(product)

# def factorial_(n):
#     product = 1
#     for i in range(n):
#         product = product*(i+1)
#     return product

# n! = (n-1)! * n
# Recursive function


def factorial_recursive(n):
    if n == 1 or n == 0:  # Base Condition which dosen't call the fuction further
        return 1
    return n*factorial_recursive(n - 1)  # function calls itself


Num = int(input("input number you want factorial for : "))
print(factorial_recursive(Num))
