productos = {
    1: {"id": 123, "nombre": "libreta", "precio": 12.500, "id_Cat": 1},
    2: {"id": 345, "nombre": "jabon", "precio": 10.500, "id_Cat": 2},
}

categorias = {
    1: {"id": 1, "nombre": "utiles escolares"},
    2: {"id": 2, "nombre": "aseo"},
}

def obtener_producto_con_categoria(productos, categorias, producto_id):
    producto = productos.get(producto_id)
    if producto:
        categoria_id = producto["id_Cat"]
        categoria = categorias.get(categoria_id)
        if categoria:
            return {
                "nombre_producto": producto["nombre"],
                "nombre_categoria": categoria["nombre"],
            }
    return None

for producto_id in productos:
    resultado = obtener_producto_con_categoria(productos, categorias, producto_id)
    if resultado:
        print(f"Nombre del producto: {resultado['nombre_producto']}")
        print(f"Nombre de la categoría: {resultado['nombre_categoria']}")
        print("-" * 30)
    else:
        print(f"El producto con ID {producto_id} no se encontró o la categoría asociada no existe.")

