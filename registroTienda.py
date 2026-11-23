print("inicializando")
productosRegistrados = 0
productosConDescuento = 0
totalCompras = 0.0
totalPagado = 0.0
producto = input("Ingrese el nombre del producto (FIN para terminar): ")
while producto != "FIN":
    cantidad = int(input("ingrese la cantidad de productos: "))
    precio = float(input("ingrese el precio unitario: "))
    productosRegistrados += 1
    totalProducto = cantidad * precio
    descuento = 0.0
    if totalProducto >= 100000:
        descuento = totalProducto * 0.10
        productosConDescuento += 1
    elif totalProducto >= 50000:
        descuento = totalProducto * 0.05
        productosConDescuento += 1
    valorfinal = totalProducto - descuento
    print("\nProducto:" + str(producto))
    print("valor original: $" + str(totalProducto))
    print("descuento: $" + str(descuento))
    print("valor a pagar: $" + str(valorfinal))

    totalCompras += totalProducto
    totalPagado += valorfinal
    producto = input("Ingrese el nombre del producto (FIN para terminar): " )
print("\n--- RESUMEN DE LA COMPRA ---")
print("Productos registrados: " + str(productosRegistrados))
print("Productos con descuento: " + str(productosConDescuento))
print("Valor original de compras: $" + str(totalCompras))
print("Total a pagar: $" + str(totalPagado))
