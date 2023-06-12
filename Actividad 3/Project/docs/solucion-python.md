# **Solución del Ejercicio Propuesto**
A continuación, se muestra el código en Python para implementar la tienda de comestibles:

```python
inventario = []

while True:
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular total")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        inventario.append((nombre, precio))

        print("Producto agregado al inventario.")
    
    elif opcion == "2":
        if len(inventario) > 0:
            print("Inventario:")
            for producto in inventario:
                print("Nombre:", producto[0])
                print("Precio:", producto[1])
                print()
        else:
            print("No hay productos en el inventario.")

    elif opcion == "3":
        total = 0
        for producto in inventario:
            total += producto[1]
        print("Total de la venta:", total)

    elif opcion == "4":
        break

    else:
        print("Opción inválida. Inténtalo nuevamente.")
```