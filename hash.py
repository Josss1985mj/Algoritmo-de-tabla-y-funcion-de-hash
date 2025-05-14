# Función para crear la tabla hash usando el último dígito
def crear_tabla_hash_por_ultimo_digito(lista_numeros):
    tabla_hash = [[] for _ in range(10)]  # 10 filas: índices 0 a 9

    for numero in lista_numeros:
        ultimo_digito = numero % 10
        tabla_hash[ultimo_digito].append(numero)

    return tabla_hash

# Función para mostrar la tabla hash
def mostrar_tabla(tabla_hash):
    print("Índice | Valores")
    print("----------------")
    for i, fila in enumerate(tabla_hash):
        print(f"  {i}    | {fila}")

# Programa principal
if __name__ == "__main__":
    numeros = [10, 23, 35, 42, 51, 66, 78, 89, 90, 101, 112, 123]
    
    tabla = crear_tabla_hash_por_ultimo_digito(numeros)
    mostrar_tabla(tabla)
