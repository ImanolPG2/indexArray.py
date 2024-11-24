def seachIndexInArray(arr: list, value: int):
    if not isinstance(value, int):
        print("Error: El valor proporcionado debe ser un número entero.")
        return
    if len(arr) != 10:
        print("Error: El arreglo debe tener 10 elementos")
        return
    found = False
    for i in range(len(arr)):
        if arr[i] == value:
            print(f"Se encontro el numero {value} en la posicion:", i+1, "del arreglo")	
            found = True
    if not found:
        print(-1)

# Prueba con un arreglo no válido
# array = [3, 3, 4, 5, 7, 4, 3, 4, 19, 56, 8, 9, 2]  # Más de 10 elementos
# value = 's'
# seachIndexInArray(array, value)

# Prueba con un arreglo válido
value = 4
array = [3, 3, 4, 5, 7, 4, 3, 4, 19, 56]  # Exactamente 10 elementos
seachIndexInArray(array, value)