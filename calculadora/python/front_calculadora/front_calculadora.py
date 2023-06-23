# Librerías externas.
import customtkinter
import math

# Librerías propias.
from calculadora.python.metadata.path import PathImages

# Apariencia de la ventana principal.
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


class VentanaCalculadora(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        # Organizo la ventana principal.
        self.geometry('282x434')
        self.calculadora_titulo = 'Calculadora'
        self.title(self.calculadora_titulo)

        # Creo configuración para la entrada y los botones.
        self.font_entrada = ('Arial', 32, 'bold')
        self.font_botones = ('Arial', 24)
        self.iconbitmap(PathImages.icono)

        self.resultado = ''

        self.home_frame = customtkinter.CTkFrame(self, width=282, height=435)
        self.home_frame.pack()
        self.texto_variable = customtkinter.StringVar()

        # Creo la ventana de entrada de texto.
        self.entrada_texto = customtkinter.CTkEntry(
            self.home_frame, width=280, height=60, font=self.font_entrada,
            justify=customtkinter.RIGHT, textvariable=self.texto_variable)
        self.entrada_texto.place(x=0, y=0)

        self.boton_porcent = customtkinter.CTkButton(
            self.home_frame, text='%', font=self.font_botones,
            command=lambda: self.ingresar_valores('%'), width=70, height=60)
        self.boton_porcent.place(x=0, y=65)

        # Creo los botones de la calculadora.
        boton_ce = customtkinter.CTkButton(
            self.home_frame, text='CE', font=self.font_botones,
            command=lambda: self.ingresar_valores('CE'), width=70, height=60)
        boton_ce.place(x=70, y=65)

        boton_c = customtkinter.CTkButton(
            self.home_frame, text='C', font=self.font_botones,
            command=self.borrar_campo, width=70, height=60)
        boton_c.place(x=140, y=65)

        boton_borrar = customtkinter.CTkButton(
            self.home_frame, text=chr(9003), font=self.font_botones,
            command=self.borrar_campo_parcial, width=70, height=60)
        boton_borrar.place(x=210, y=65)

        boton_inverso = customtkinter.CTkButton(
            self.home_frame, text='1/x', font=self.font_botones,
            command=self.obtener_inverso, width=70, height=60)
        boton_inverso.place(x=0, y=126)

        boton_cuadrado = customtkinter.CTkButton(
            self.home_frame, text='x\u00B2', font=self.font_botones,
            command=self.obtener_cuadrado, width=70, height=60)
        boton_cuadrado.place(x=70, y=126)

        boton_raiz_cuadrada = customtkinter.CTkButton(
            self.home_frame, text='\u221A', font=self.font_botones,
            command=self.obtener_raiz_cuadrada, width=70, height=60)
        boton_raiz_cuadrada.place(x=140, y=126)

        boton_division = customtkinter.CTkButton(
            self.home_frame, text='\u00F7', font=self.font_botones,
            command=lambda: self.ingresar_valores('/'), width=70, height=60)
        boton_division.place(x=210, y=126)

        boton_7 = customtkinter.CTkButton(
            self.home_frame, text='7', font=self.font_botones,
            command=lambda: self.ingresar_valores(7), width=70, height=60)
        boton_7.place(x=0, y=187)

        boton_8 = customtkinter.CTkButton(
            self.home_frame, text='8', font=self.font_botones,
            command=lambda: self.ingresar_valores(8), width=70, height=60)
        boton_8.place(x=70, y=187)

        boton_9 = customtkinter.CTkButton(
            self.home_frame, text='9', font=self.font_botones,
            command=lambda: self.ingresar_valores(9), width=70, height=60)
        boton_9.place(x=140, y=187)

        boton_multiplicacion = customtkinter.CTkButton(
            self.home_frame, text='x', font=self.font_botones,
            command=lambda: self.ingresar_valores('*'), width=70, height=60)
        boton_multiplicacion.place(x=210, y=187)

        boton_4 = customtkinter.CTkButton(
            self.home_frame, text='4', font=self.font_botones,
            command=lambda: self.ingresar_valores(4),
            width=70, height=60)
        boton_4.place(x=0, y=248)

        boton_5 = customtkinter.CTkButton(
            self.home_frame, text='5', font=self.font_botones,
            command=lambda: self.ingresar_valores(5), width=70, height=60)
        boton_5.place(x=70, y=248)

        boton_6 = customtkinter.CTkButton(
            self.home_frame, text='6', font=self.font_botones,
            command=lambda: self.ingresar_valores(6), width=70, height=60)
        boton_6.place(x=140, y=248)

        boton_resta = customtkinter.CTkButton(
            self.home_frame, text='\u2212', font=self.font_botones,
            command=lambda: self.ingresar_valores('-'), width=70, height=60)
        boton_resta.place(x=210, y=248)

        boton_1 = customtkinter.CTkButton(
            self.home_frame, text='1', font=self.font_botones,
            command=lambda: self.ingresar_valores(1), width=70, height=60)
        boton_1.place(x=0, y=309)

        boton_2 = customtkinter.CTkButton(
            self.home_frame, text='2', font=self.font_botones,
            command=lambda: self.ingresar_valores(2), width=70, height=60)
        boton_2.place(x=70, y=309)

        boton_3 = customtkinter.CTkButton(
            self.home_frame, text='3', font=self.font_botones,
            command=lambda: self.ingresar_valores(3), width=70, height=60)
        boton_3.place(x=140, y=309)

        boton_suma = customtkinter.CTkButton(
            self.home_frame, text='+', font=self.font_botones,
            command=lambda: self.ingresar_valores('+'), width=70, height=60)
        boton_suma.place(x=210, y=309)

        boton_mas_menos = customtkinter.CTkButton(
            self.home_frame, text='\u00B1', font=self.font_botones,
            command=self.obtener_nuevo_signo, width=70, height=60)
        boton_mas_menos.place(x=0, y=371)

        boton_0 = customtkinter.CTkButton(
            self.home_frame, text='0', font=self.font_botones,
            command=lambda: self.ingresar_valores(0), width=70, height=60)
        boton_0.place(x=70, y=371)

        boton_cierra = customtkinter.CTkButton(
            self.home_frame, text='.', font=self.font_botones,
            command=lambda: self.ingresar_valores('.'), width=70, height=60)
        boton_cierra.place(x=140, y=371)

        boton_igualdad = customtkinter.CTkButton(
            self.home_frame, text='=', font=self.font_botones,
            command=self.calcular, width=70, height=60)
        boton_igualdad.place(x=210, y=371)

    def ingresar_valores(self, simbolo: int | str) -> None:
        caracteres = ['.', '+', '-', '*', '/']

        if simbolo in list(range(10)) + caracteres:
            self.texto_variable.set(self.texto_variable.get() + str(simbolo))

        if simbolo == '%':
            simbolo.replace('%', '/100')
            self.texto_variable.set(
                self.texto_variable.get() + str(simbolo.replace('%', '/100')))

    def calcular(self):
        self.resultado = str(eval(self.texto_variable.get()))
        self.borrar_campo()
        self.entrada_texto.insert(0, self.resultado)
        self.texto_variable.set(self.resultado)

    def obtener_porcentaje(self) -> None:
        self.resultado = str(float(self.texto_variable.get()) / 100)
        self.entrada_texto.insert(0, self.resultado)
        self.texto_variable.set(self.resultado)

    def borrar_campo(self):
        self.entrada_texto.delete(0, customtkinter.END)

    def borrar_campo_parcial(self):
        self.resultado = self.texto_variable.get()[:-1]
        print(self.resultado)
        self.texto_variable.set(self.resultado)

    def obtener_inverso(self) -> None:
        self.resultado = str(1 / float(self.texto_variable.get()))
        self.texto_variable.set(self.resultado)

    def obtener_cuadrado(self) -> None:
        self.resultado = str(float(self.texto_variable.get()) ** 2)
        self.entrada_texto.delete(0, 'end')
        self.texto_variable.set(self.resultado)

    def obtener_raiz_cuadrada(self) -> None:
        self.resultado = str(math.sqrt(float(self.texto_variable.get())))
        self.entrada_texto.insert(0, self.resultado)
        self.texto_variable.set(self.resultado)

    def obtener_nuevo_signo(self) -> None:
        self.resultado = str(-1 * float(self.texto_variable.get()))
        self.entrada_texto.insert(0, self.resultado)
        self.texto_variable.set(self.resultado)
