# **Explicación del Código Paso a Paso**

El código Python indicado  se encarga de gestionar un inventario de productos. A continuación, te explico paso a paso qué se realiza en este código:

1. Se define una lista vacía llamada inventario para almacenar los productos.

2. Se inicia un bucle while True, que se ejecutará indefinidamente hasta que se elija la opción "4" para salir.

3. Dentro del bucle, se muestran las opciones disponibles para el usuario: agregar producto, mostrar inventario, calcular total y salir.

4. Se solicita al usuario que elija una opción ingresando el número correspondiente.

    Si la opción seleccionada es "*1*", se solicita al usuario que ingrese el nombre y el precio del producto. El nombre se guarda en la variable nombre y el precio se convierte a tipo float y se guarda en la variable precio. Luego, se agrega una tupla con el nombre y el precio al inventario utilizando inventario.append((nombre, precio)), y se muestra un mensaje indicando que el producto se ha agregado al inventario.

    Si la opción seleccionada es "*2*", se verifica si hay productos en el inventario utilizando len(inventario) > 0. Si hay productos, se recorre la lista inventario utilizando un bucle for y se muestra el nombre y el precio de cada producto en el inventario. Si no hay productos, se muestra un mensaje indicando que no hay productos en el inventario.

    Si la opción seleccionada es "*3*", se calcula el total de la venta sumando el precio de cada producto en el inventario. Se utiliza un bucle for para recorrer la lista inventario y se acumula el precio de cada producto en la variable total. Luego, se muestra el total de la venta.

    Si la opción seleccionada es "*4*", se utiliza la sentencia break para salir del bucle while y finalizar la ejecución del programa.

    Si la opción seleccionada no corresponde a ninguna de las opciones anteriores, se muestra un mensaje indicando que la opción es inválida y se solicita al usuario que intente nuevamente.

Este código permite al usuario agregar productos al inventario, mostrar el inventario actual, calcular el total de la venta y salir del programa. Es un ejemplo básico de gestión de inventario en Python.