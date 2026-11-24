import datetime

def domingo():
    contador = 0
    
    for año in range(1900, 2001):
        for mes in range(1, 13):
            fecha = datetime.date(año, mes, 1)
            if fecha.weekday() == 6:
                contador += 1
    return contador

resultado = domingo()
print(f"Total de domingos que cayeron en el primer día de mes: {resultado}")