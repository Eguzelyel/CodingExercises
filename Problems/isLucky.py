# Definitely not the best way. Didn't use the string method.

def is_lucky(n):
    import math

    digits = int(math.log10(n)) + 1

    if digits == 0 or digits == 1:
        return True

    first_sum = 0
    second_sum = 0
    for i in range(digits):
        val = n // (10 ** (digits - i - 1))  # ->1560 - 1
        print(val)
        if i < digits / 2:
            first_sum += val
        else:
            second_sum += val
        n -= val * (10 ** (digits - i - 1))  # ->1560 - 1000

    return first_sum == second_sum
