import tkinter as tk


def ventana_principal_calculadora():
    # Creamos una ventana principal, la cuál contendrá los demás widgets.
    ventana_principal = tk.Tk()

    # También podemos crear las dimensiones de la ventana pricipal.
    ventana_principal.geometry('330x469')

    # Vamos a colocarle el título a la ventana.
    ventana_principal.title('Calculadora')

    # Creamos un recuadro para ingresar texto.
    entrada_texto = tk.Entry(ventana_principal, justify=tk.RIGHT)
    entrada_texto.pack(padx=3, pady=75, fill='x')

    # Activamos la ventana principal.
    ventana_principal.mainloop()
