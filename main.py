import timeit

def soma1(n):
    soma = 0
    for i in range(n + 1 ):
        soma += 1 

    return soma

tempo_inicial = timeit.default_timer()
soma1(10000000000000)
tempo_final = timeit.default_timer()
print(f"Tempo soma1:{tempo_final - tempo_inicial}")