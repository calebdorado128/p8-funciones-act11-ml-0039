# Caleb Dorado NC = 0039

print("Ejemplo 1: Parámetros con valores por defecto")

def saludar(nombre, saludo="Hola"):
    """Saluda a una persona con un saludo personalizable"""
    return f"{saludo}, {nombre}!"

print(saludar("María"))
print(saludar("Pedro", "Buenos días"))
print(saludar("Ana", saludo="Qué tal"))

print("")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")

print("Ejemplo 2: Retorno múltiple mediante tuplas")

def calcular_estadisticas(numeros):
    """Calcula suma, promedio y máximo de una lista"""
    total = sum(numeros)
    promedio = total / len(numeros)
    maximo = max(numeros)
    return total, promedio, maximo

suma, prom, max_val = calcular_estadisticas([10, 20, 30, 40, 50])
print(f"Suma: {suma}, Promedio: {prom}, Máximo: {max_val}")

print("")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")

print("Ejemplo 3: Argumentos variables con args")

def sumar_todos(*numeros):
    """Suma cualquier cantidad de números"""
    total = 0
    for num in numeros:
        total += num
    return total

print(sumar_todos(1, 2, 3))
print(sumar_todos(10, 20, 30, 40))
print(sumar_todos(5))

print("")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")

print("Ejemplo 4: Closures y Funciones Anidadas")

def crear_multiplicador(factor):
    """Retorna una función que multiplica por 'factor'"""
    def multiplicar(numero):
        return numero * factor 
    return multiplicar

duplicar = crear_multiplicador(2)
triplicar = crear_multiplicador(3)

print(duplicar(10))
print(triplicar(10))

print("")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")

print("Ejemplo 5: Funciones como argumentos (Objetos de primera clase)")

def aplicar_operacion(a, b, operacion):
    """Aplica una función a dos números"""
    return operacion(a, b)

def sumar(x, y):
    return x + y

def multiplicar(x, y):
    return x * y

print(aplicar_operacion(5, 3, sumar))
print(aplicar_operacion(5, 3, multiplicar))

print("")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")

print("Ejemplo 6: Filtrar elementos de una lista")

def filtrar_pares(numeros):
    """Retorna solo los números pares de una lista"""
    pares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
    return pares

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtrar_pares(lista))

print("")
print("Hecho por Caleb Dorado NC = 0039")