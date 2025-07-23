def busqueda_binaria(lista, elemento):
    """
    Implementación de búsqueda binaria.
    Requiere que la lista esté ordenada.
    Devuelve el índice del elemento si se encuentra, de lo contrario -1.
    """
    izquierda = 0
    derecha = len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = lista[medio]
        
        if valor_medio == elemento:
            return medio
        elif elemento < valor_medio:
            derecha = medio - 1
        else:
            izquierda = medio + 1
    
    return -1  # Elemento no encontrado

# Ejemplo de uso
if __name__ == "__main__":
    lista_ordenada = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    elemento_a_buscar = 23
    
    resultado = busqueda_binaria(lista_ordenada, elemento_a_buscar)
    
    if resultado != -1:
        print(f"Elemento encontrado en el índice {resultado}")
    else:
        print("Elemento no encontrado en la lista")