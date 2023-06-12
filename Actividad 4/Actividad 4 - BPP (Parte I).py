#Apartado 1

import pdb

def encontrar_maximos(lista_de_listas):
    pdb.set_trace()  #Punto de parada en la línea de la comprensión de listas
    maximos = [max(sublista) for sublista in lista_de_listas]
    return maximos

lista = [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]]

maximos = encontrar_maximos(lista)
print(maximos)
