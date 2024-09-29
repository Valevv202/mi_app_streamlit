# funciones.py

def saludar(nombre):
    return f"Hola, {nombre}"

def sumar(a, b):
    return a + b

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_precio_final(precio, descuento=10, impuesto=16):
    precio_final = precio - (precio * (descuento / 100)) + (precio * (impuesto / 100))
    return precio_final

def sumar_lista(numeros):
    return sum(numeros)

def producto(nombre, cantidad=1, precio=10):
    return cantidad * precio

def numeros_pares_e_impares(lista):
    pares = [num for num in lista if num % 2 == 0]
    impares = [num for num in lista if num % 2 != 0]
    return pares, impares

def multiplicar_todos(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado if args else 1

def informacion_personal(**kwargs):
    return '\n'.join([f"{key}: {value}" for key, value in kwargs.items()])

def calculadora_flexible(num1, num2, operacion='suma'):
    operaciones = {
        'suma': num1 + num2,
        'resta': num1 - num2,
        'multiplicacion': num1 * num2,
        'division': num1 / num2 if num2 != 0 else 'Error: División por cero'
    }
    return operaciones.get(operacion, 'Operación no válida')