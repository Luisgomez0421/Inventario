

print("=== Sistema simple de inventario ===")

nombre = input("Ingrese el nombre del producto: ")

while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio < 0:
            print("El precio no puede ser negativo. Intente nuevamente.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")

while True:
    try:
        cantidad = int(input("Ingrese la cantidad: "))
        if cantidad < 0:
            print("La cantidad no puede ser negativa. Intente nuevamente.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")

costo_total = precio * cantidad

print("\n=== Resultado ===")
print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")