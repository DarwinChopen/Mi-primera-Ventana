import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="Escribe tu nombre:")
etiqueta.pack(pady=5)

entrada = tk.Entry(ventana)
entrada.pack(pady=5)

def saludar():
    nombre = entrada.get()
    etiqueta.config(text=f"Hola, {nombre}!")

def limpiar():
    entrada.delete(0, tk.END)
    etiqueta.config(text="Escribe tu nombre:")
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)




boton_saludar = tk.Button(ventana, text="Saludar", command=saludar)
boton_saludar.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(pady=5)

etiqueta_resutado = tk.Label(ventana, text="el resultado es:")
etiqueta_resutado.pack(pady=5)

etiqueta1 = tk.Label(ventana, text="Escribe El primer numero:")
etiqueta1.pack(pady=5)

entrada1 = tk.Entry(ventana)
entrada1.pack(pady=5)

etiqueta2 = tk.Label(ventana, text="Escribe el Segundo mumero:")
etiqueta2.pack(pady=5)

entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)

def sumar():
    try:
        num1 = int(entrada1.get())
        num2 = int(entrada2.get())
        resultado = num1 + num2
        etiqueta_resutado.config(text=f"El resultado es: {resultado}")
    except ValueError:
        etiqueta_resutado.config(text="Por favor, ingresa números válidos.")

def restar():
    try:
        num1 = int(entrada1.get())
        num2 = int(entrada2.get())
        resultado = num1 - num2
        etiqueta_resutado.config(text=f"El resultado es: {resultado}")
    except ValueError:
        etiqueta_resutado.config(text="Por favor, ingresa números válidos.")

def multiplicar():
    try:
        num1 = int(entrada1.get())
        num2 = int(entrada2.get())
        resultado = num1 * num2
        etiqueta_resutado.config(text=f"El resultado es: {resultado}")
    except ValueError:
        etiqueta_resutado.config(text="Por favor, ingresa números válidos.")

def dividir():
    try:
        num1 = int(entrada1.get())
        num2 = int(entrada2.get())
        resultado = num1 / num2
        etiqueta_resutado.config(text=f"El resultado es: {resultado}")
    except ValueError:
        etiqueta_resutado.config(text="Por favor, ingresa números válidos.")

boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=5)

boton_restar = tk.Button(ventana, text="Restar", command=restar)
boton_restar.pack(pady=5)

boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=multiplicar)
boton_multiplicar.pack(pady=5)

boton_dividir = tk.Button(ventana, text="Dividir", command=dividir)
boton_dividir.pack(pady=5)


ventana.mainloop()