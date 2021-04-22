'''FizzBuzz program:
Return Fizz if number is a multiple of 3
Return Buzz if number is a multiple of 5
Return FizzBuzz if number is a multiple of both 3 and 5
Return the number itself if not a multiple of 3 or 5'''

def fizzbuzz(n):
    if (n % 3 == 0) and (n % 5 == 0):
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return n
