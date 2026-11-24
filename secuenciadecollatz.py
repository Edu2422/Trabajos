def longitud_collatz(n):
    pasos = 1  
    
    while n > 1:
        if n % 2 == 0:
            n = n // 2      
        else:
            n = 3 * n + 1  
            
        pasos += 1        
        
    return pasos


lim = 1000000
mejor_numero = 0
maxima_longitud = 0


for numero_actual in range(1, lim):
    longitud_actual = longitud_collatz(numero_actual)
    
    if longitud_actual > maxima_longitud:
        maxima_longitud = longitud_actual
        mejor_numero = numero_actual


print(f"El número inicial con la cadena más larga es: {mejor_numero}")
print(f"Cantidad de términos en su cadena: {maxima_longitud}")