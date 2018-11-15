import math

def primeNumbers(limit):	# calls is_prime the least number of times; uses sieve function
    result = []
    if limit >= 2:
        result.append(2)
        sieved_list = sieve_list(limit)
        for number in sieved_list:
            if not(is_prime(number)):
                continue
            else:
                result.append(number)
    return result


def is_prime(num):  # most annoying function: call as few times as possible
    if (num == 0) or (num == 1):
        return False
    elif num == 2:
        return True
    for divisor in range(int(math.sqrt(num))+1):
        if (divisor == 0) or (divisor == 1):
            continue
        elif num % divisor == 0:
            return False
    return True 


def sieve_list(limit):  # removes >65% of numbers
    odd_list = list(range(1, limit+1, 2))   # list of odd numbers from 3
    odd_multiples_of_three = list(range(9, limit+1, 6))     # list of multiples of 3 from 9
    for number in odd_multiples_of_three:   # remove multiples of 3 from odd_list
        if number in odd_list:
            odd_list.remove(number)
    return odd_list

print(primeNumbers(1000))