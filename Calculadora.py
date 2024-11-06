from tkinter import *
from tkinter import ttk
import math

def ingresarValor(tecla):
    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada_2.set(entrada_2.get() + tecla)
    
    if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
        if tecla == '*':
            entrada_1.set(entrada_2.get() + '*')
        elif tecla == '/':
            entrada_1.set(entrada_2.get() + '/')
        elif tecla == '+':
            entrada_1.set(entrada_2.get() + '+')
        elif tecla == '-':
            entrada_1.set(entrada_2.get() + '-')
    
        entrada_2.set(' ')

    if tecla == '=':
        entrada_1.set(entrada_1.get() + entrada_2.get())
        resultado = eval(entrada_1.get())
        entrada_2.set(resultado)

def raizCuadrada():
    entrada_1.set('')
    resultado = math.sqrt(float(entrada_2.get()))
    entrada_2.set(resultado)

def borrar():
    inicio = 0
    final = len(entrada_2.get())
    entrada_2.set(entrada_2.get()[inicio:final-1])

def borrarTodo():
    entrada_1.set('')
    entrada_2.set('')

def ingresarValoresTeclado(event):
    tecla = event.char

    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada_2.set(entrada_2.get() + tecla)
    
    if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
        if tecla == '*':
            entrada_1.set(entrada_2.get() + '*')
        elif tecla == '/':
            entrada_1.set(entrada_2.get() + '/')
        elif tecla == '+':
            entrada_1.set(entrada_2.get() + '+')
        elif tecla == '-':
            entrada_1.set(entrada_2.get() + '-')
    
        entrada_2.set(' ')

    if tecla == '=':
        entrada_1.set(entrada_1.get() + entrada_2.get())
        resultado = eval(entrada_1.get())
        entrada_2.set(resultado)

#Configuración de la ventana
root = Tk()
root.title("Calculadora")
root.geometry("+500+80")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure('mainframe.TFrame', background="#DBDBDB")

mainframe = ttk.Frame(root, style="mainframe.TFrame")
mainframe.grid(column=0, row=0, sticky=(W, N, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)

#Estilos label
estilos_label1 = ttk.Style()
estilos_label1.configure('Label.TLabel', font="arial 15", anchor="e")

estilos_label2 = ttk.Style()
estilos_label2.configure('Label2.TLabel', font="arial 40", anchor="e")

entrada_1 = StringVar()
label_entrada_1 = ttk.Label(mainframe, textvariable=entrada_1, style="Label.TLabel")
label_entrada_1.grid(column=0, row=0, columnspan=4, sticky=(W, N, E, S))

entrada_2 = StringVar()
label_entrada_2 = ttk.Label(mainframe, textvariable=entrada_2, style="Label2.TLabel")
label_entrada_2.grid(column=0, row=1)
label_entrada_2.grid(column=0, row=1, columnspan=4, sticky=(W, E))

#Estilos para los botones
estilo_botones_numeros = ttk.Style()
estilo_botones_numeros.configure('Botones_numeros.TButton', font="arial 22", width=5, background="#FFFFFF", relief="flat")

estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure('Botones_borrar.TButton', font="arial 22", width=5, relief="flat", background="#CECECE")
estilos_botones_borrar.map('Botones_borrar.TButton', foreground=[('active', '#FF0000')])

estilos_botones_restantes = ttk.Style()
estilos_botones_restantes.configure('Botones_restantes.TButton', font="arial 22", width=5, relief="flat", background="#CECECE")

button0 = ttk.Button(mainframe, text="0", style="Botones_numeros.TButton", command=lambda: ingresarValor('0'))
button1 = ttk.Button(mainframe, text="1", style="Botones_numeros.TButton", command=lambda: ingresarValor('1'))
button2 = ttk.Button(mainframe, text="2", style="Botones_numeros.TButton", command=lambda: ingresarValor('2'))
button3 = ttk.Button(mainframe, text="3", style="Botones_numeros.TButton", command=lambda: ingresarValor('3'))
button4 = ttk.Button(mainframe, text="4", style="Botones_numeros.TButton", command=lambda: ingresarValor('4'))
button5 = ttk.Button(mainframe, text="5", style="Botones_numeros.TButton", command=lambda: ingresarValor('5'))
button6 = ttk.Button(mainframe, text="6", style="Botones_numeros.TButton", command=lambda: ingresarValor('6'))
button7 = ttk.Button(mainframe, text="7", style="Botones_numeros.TButton", command=lambda: ingresarValor('7'))
button8 = ttk.Button(mainframe, text="8", style="Botones_numeros.TButton", command=lambda: ingresarValor('8'))
button9 = ttk.Button(mainframe, text="9", style="Botones_numeros.TButton", command=lambda: ingresarValor('9'))

button_borrar = ttk.Button(mainframe, text=chr(9003), style="Botones_borrar.TButton", command=lambda: borrar())
button_borrar_todo = ttk.Button(mainframe, text="C", style="Botones_borrar.TButton", command= lambda: borrarTodo())
button_parentesis1 = ttk.Button(mainframe, text="(", style="Botones_restantes.TButton", command=lambda: ingresarValor('('))
button_parentesis2 = ttk.Button(mainframe, text=")", style="Botones_restantes.TButton", command=lambda: ingresarValor(')'))
button_punto = ttk.Button(mainframe, text=".", style="Botones_restantes.TButton", command=lambda: ingresarValor('.'))

button_division = ttk.Button(mainframe, text=chr(247), style="Botones_restantes.TButton", command=lambda: ingresarValor('/'))
button_multiplicacion = ttk.Button(mainframe, text="x", style="Botones_restantes.TButton", command=lambda: ingresarValor('*'))
button_resta = ttk.Button(mainframe, text="-", style="Botones_restantes.TButton", command=lambda: ingresarValor('-'))
button_suma = ttk.Button(mainframe, text="+", style="Botones_restantes.TButton", command=lambda: ingresarValor('+'))

button_igual = ttk.Button(mainframe, text="=", style="Botones_restantes.TButton", command=lambda: ingresarValor('='))
button_raiz_cuadrada = ttk.Button(mainframe, text=chr(221), style="Botones_restantes.TButton")

#Colocar botones en la pantalla
button_parentesis1.grid(column=0, row=2, sticky=(W, N, E, S))
button_parentesis2.grid(column=1, row=2, sticky=(W, N, E, S))
button_borrar_todo.grid(column=2, row=2, sticky=(W, N, E, S))
button_borrar.grid(column=3, row=2, sticky=(W, N, E, S))

button7.grid(column=0, row=3, sticky=(W, N, E, S))
button8.grid(column=1, row=3, sticky=(W, N, E, S))
button9.grid(column=2, row=3, sticky=(W, N, E, S))
button_division.grid(column=3, row=3, sticky=(W, N, E, S))

button4.grid(column=0, row=4, sticky=(W, N, E, S))
button5.grid(column=1, row=4, sticky=(W, N, E, S))
button6.grid(column=2, row=4, sticky=(W, N, E, S))
button_multiplicacion.grid(column=3, row=4, sticky=(W, N, E, S))

button3.grid(column=0, row=5, sticky=(W, N, E, S))
button2.grid(column=1, row=5, sticky=(W, N, E, S))
button1.grid(column=2, row=5, sticky=(W, N, E, S))
button_suma.grid(column=3, row=5, sticky=(W, N, E, S))

button0.grid(column=0, row=6, columnspan=2, sticky=(W, N, E, S))
button_punto.grid(column=2, row=6, sticky=(W, N, E, S))
button_resta.grid(column=3, row=6, sticky=(W, N, E, S))

button_igual.grid(column=0, row=7, columnspan=3, sticky=(W, N, E, S))
button_raiz_cuadrada.grid(column=3, row=7, sticky=(W, N, E, S))

for chlid in mainframe.winfo_children():
    chlid.grid_configure(ipady=10, padx=1, pady=1)

root.bind('<Key>', ingresarValoresTeclado)
root.mainloop()