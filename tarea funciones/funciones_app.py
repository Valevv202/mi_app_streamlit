# app.py

import streamlit as st
import pandas as pd
from funciones1 import *  # Importa todas las funciones desde funciones.py

# Configuración de la aplicación Streamlit
st.title("Tablero Interactivo de Ejercicios en Python")

# Sidebar para seleccionar el ejercicio
ejercicio = st.sidebar.selectbox("Selecciona un ejercicio", [
    "Saludo",
    "Suma de dos números",
    "Área de un triángulo",
    "Calculadora de descuento",
    "Suma de una lista",
    "Funciones con valores predeterminados",
    "Números pares e impares",
    "Multiplicación con *args",
    "Información personal con **kwargs",
    "Calculadora flexible"
])

# Ejercicio específico
if ejercicio == "Saludo":
    nombre = st.text_input("Ingresa tu nombre:")
    apellido = st.text_input("Ingresa tu primer apellido:")
    apellido2 = st.text_input("Ingresa tu segundo apellido:")

    if st.button("Saludar"):
        # Combinar nombre y apellido
        saludo = f"Hola, {nombre} {apellido} {apellido2}!"
        st.write(saludo)

elif ejercicio == "Suma de dos números":
    a = st.number_input("Ingresa el primer número:", value=0)
    b = st.number_input("Ingresa el segundo número:", value=0)
    if st.button("Sumar"):
        st.write(f"La suma es: {sumar(a, b)}")

elif ejercicio == "Área de un triángulo":
    base = st.number_input("Ingresa la base del triángulo:", value=0)
    altura = st.number_input("Ingresa la altura del triángulo:", value=0)
    if st.button("Calcular área"):
        st.write(f"El área del triángulo es: {calcular_area_triangulo(base, altura)}")

elif ejercicio == "Calculadora de descuento":
    precio = st.number_input("Ingresa el precio original:", value=0)
    descuento = st.number_input("Ingresa el porcentaje de descuento:", value=10)
    impuesto = st.number_input("Ingresa el porcentaje de impuesto:", value=16)
    if st.button("Calcular precio final"):
        st.write(f"El precio final es: {calcular_precio_final(precio, descuento, impuesto)}")

elif ejercicio == "Suma de una lista":
    numeros = st.text_input("Ingresa una lista de números separados por comas:")
    
    if numeros:
        lista_numeros = list(map(int, numeros.split(',')))
        if st.button("Sumar lista"):
            st.write(f"La suma es: {sumar_lista(lista_numeros)}")

if ejercicio == "Funciones con valores predeterminados":
    # Inicializar la lista de productos si no existe
    if 'productos' not in st.session_state:
        st.session_state.productos = []

    # Sección para ingresar los detalles del producto
    nombre_producto = st.text_input("Nombre del producto:")
    cantidad = st.number_input("Cantidad (por defecto 1):", value=1)
    precio_unitario = st.number_input("Precio por unidad (por defecto 10):", value=10)

    # Botón para agregar un nuevo producto
    if st.button("Agregar producto"):
        if nombre_producto:  # Verifica que el nombre no esté vacío
            total_producto = producto(nombre_producto, cantidad, precio_unitario)
            st.session_state.productos.append({
                'Producto': nombre_producto,
                'Cantidad': cantidad,
                'Precio por unidad': precio_unitario,
                'Total': total_producto
            })
            st.success(f"Producto '{nombre_producto}' agregado.")
        else:
            st.warning("Por favor, ingresa un nombre para el producto.")

    # Mostrar la tabla de productos si hay alguno agregado
    if st.session_state.productos:
        if st.button("Mostrar lista de productos"):
            df_productos = pd.DataFrame(st.session_state.productos)
            st.subheader("Lista de Productos")
            st.dataframe(df_productos)
    else:
        if st.button("Mostrar lista de productos"):
            st.warning("No hay productos agregados.")

elif ejercicio == "Números pares e impares":
    numeros = st.text_input("Ingresa una lista de números separados por comas:")
    
    if numeros:
        lista_numeros = list(map(int, numeros.split(',')))
        if st.button("Separar pares e impares"):
            pares, impares = numeros_pares_e_impares(lista_numeros)
            st.write(f"Números pares: {pares}")
            st.write(f"Números impares: {impares}")

elif ejercicio == "Multiplicación con *args":
    numeros = st.text_input("Ingresa números separados por comas:")
    
    if numeros:
        lista_numeros = list(map(int, numeros.split(',')))
        if st.button("Multiplicar todos"):
            resultado = multiplicar_todos(*lista_numeros)
            st.write(f"El resultado de la multiplicación es: {resultado}")

elif ejercicio == "Información personal con **kwargs":
    nombre = st.text_input("Nombre:")
    edad = st.number_input("Edad:")
    altura = st.number_input("Altura (cm):")
    peso = st.number_input("Peso (kg):")
    direccion = st.text_input("Dirección:")
    codigo_postal = st.text_input("Código Postal:")
    
    if st.button("Mostrar información"):
        # Mostrar datos en formato clave-valor
        info_texto = f"""
        Nombre: {nombre}
        Edad: {edad}
        Altura: {altura} cm
        Peso: {peso} kg
        Dirección: {direccion}
        Código Postal: {codigo_postal}
        """
        # Mostrar información en la aplicación
        st.markdown(info_texto)

elif ejercicio == "Calculadora flexible":
    num1 = st.number_input("Primer número:", value=0)
    num2 = st.number_input("Segundo número:", value=0)
    
    operacion = st.selectbox("Selecciona una operación", ["suma", "resta", "multiplicacion", "division"])
    
    if st.button("Calcular"):
        resultado = calculadora_flexible(num1, num2, operacion)
        st.write(f"El resultado es: {resultado}")