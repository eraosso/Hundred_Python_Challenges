"""Write a function that returns the factors of  a number.
Return the output in a list."""

def factors(n):
    resposta = []
    for i in range(1, int(n/2 + 1)):
        if n % i == 0:
            resposta.append(i)
    resposta.append(n)
    return resposta
