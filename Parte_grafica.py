import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("400x400+500+300")
ventana.configure(bg="grey")

etiqueta_titulo = tk.Label(
    ventana,
    text="CALCULADORA",
    bg="grey",
    fg="black",
    font=("Arial", 20, "bold")
)
etiqueta_titulo.pack(pady=5)

etiqueta1 = tk.Label(
    ventana,
    text="Escribe el primer número:",
    bg="grey",
    fg="darkblue",
    font=("Arial", 12, "bold")
)
etiqueta1.pack(pady=5)

entrada1 = tk.Entry(ventana, font=("Arial", 12))
entrada1.pack(pady=5)

# Etiqueta 2
etiqueta2 = tk.Label(
    ventana,
    text="Escribe el segundo número:",
    bg="grey",
    fg="darkblue",
    font=("Arial", 12, "bold")
)
etiqueta2.pack(pady=5)

entrada2 = tk.Entry(ventana, font=("Arial", 12))
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

def limpiar():

    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    etiqueta_resutado.config(text="El Resultado de la operacion es: ")

frame_botones = tk.Frame(ventana, bg="grey",)
frame_botones.pack(pady=5)

boton_sumar = tk.Button(frame_botones, text="Sumar", command=sumar)
boton_sumar.pack(side="left",padx=5)

boton_restar = tk.Button(frame_botones, text="Restar", command=restar)
boton_restar.pack(side="left",padx=5)

boton_multiplicar = tk.Button(frame_botones, text="Multiplicar", command=multiplicar)
boton_multiplicar.pack(side="left",padx=5)

boton_dividir = tk.Button(frame_botones, text="Dividir", command=dividir)
boton_dividir.pack(side="left",padx=5)

etiqueta_resutado = tk.Label(ventana, text="EL RESULTADO DE LA OPERACION ES:")
etiqueta_resutado.pack(pady=10)

frame_lisa = tk.Frame(ventana, bg="grey")
frame_lisa.pack(pady=10)

boton_limpiar = tk.Button(frame_lisa, text="Limpiar", command=limpiar)
boton_limpiar.pack(side="left",padx=5)

boton_salir = tk.Button(frame_lisa, text="Salir", command=ventana.quit)
boton_salir.pack(side="left",padx=5)

ventana.mainloop()