'''Write a function that returns the decimal part of a number.
The output can be rounded  to 2 decimal places. If the decimal part  is
zero,  the function  should return "INTEGER".'''

def decimal_part(n):
    decimal = n - int(n)
    if decimal == 0:
        return 'INTEGER'
    else:
        return round(decimal, 2)