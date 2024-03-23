lista = input("ingrese 10 numeros separados por comas:")
lista = lista.split(",")
i = 0
suma  = 0 
while i < len(lista):
    suma += int(lista[i])
    i += 1
    
promedio = suma / len(lista)
print("el promedio de la lista es" , promedio)

    
