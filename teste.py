import timeit

def soma2(n):
    return (n*(n+1)) / 2 


    
    

tempo_inicial = timeit.default_timer()
soma2(10)
tempo_final = timeit.default_timer()
print(f"Tempo soma1:{tempo_final - tempo_inicial}")