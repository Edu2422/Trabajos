limite = 2_000_000
suma = 0
cantidad = 0

for numero in range(2, limite + 1):
    es_primo = True
    divisor = 2

    while divisor * divisor <= numero and es_primo:
        if numero % divisor == 0:
            es_primo = False
        divisor = divisor + 1

    if es_primo:
        print(numero)
        suma = suma + numero
        cantidad = cantidad + 1

print("Cantidad de primos:", cantidad)
print("Suma:", suma)
