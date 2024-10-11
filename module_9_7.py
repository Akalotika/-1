def sum_three(a, b, c):
    return a + b + c


def is_prime(func):
    def wrapper(*args, **kwargs):
        result_ = func(*args, **kwargs)
        if result_ > 1:
            if all((result_ % i != 0) for i in range(2, int(result_ ** 0.5) + 1)):
                return "Простое"
            else:
                return "Составное"

    return wrapper


@is_prime
def sum_three(a, b, c):
    result_ = a + b + c
    print(result_)
    return result_


result = sum_three(2, 3, 6)
print(result)
