def is_prime(func):
    def wrapper(*args):
        num = func(*args)
        for i in range(2, num// 2):
            if num % i == 0:
                print("Составное")
        else:
            print("Простое")
        return num
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
