"""Write a  fucntion that accepts two  integers and returns the quotient and remainder
of num1 divided by num2. Round the output to two decimal places."""

def quot_rem(num1, num2):
    q = round(num1 / num2, 2)
    r = round(num1 % num2, 2)
    return (q, r)

