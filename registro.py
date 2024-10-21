import os
from tkinter import END, Toplevel, Label, Button, Entry, StringVar

def registrar_usuario(usuario, contra):
    usuario_info = usuario.get()
    contra_info = contra.get()

    if not os.path.exists("users"):
        os.makedirs("users")

    with open(f"users/{usuario_info}.txt", "w") as archivo:
        archivo.write(usuario_info + "\n")
        archivo.write(contra_info)

    usuario_entrada.delete(0, END)
    contra_entrada.delete(0, END)

    Label(pantalla1, text="Registro Convencional Exitoso", fg="green", font=("Calibri", 11)).pack()

def registro(pantalla):  # Aceptar pantalla como argumento
    global usuario, contra, usuario_entrada, contra_entrada, pantalla1
    pantalla1 = Toplevel(pantalla)  # Usar la ventana pasada como argumento
    pantalla1.title("Registro")
    pantalla1.geometry("300x250")

    usuario = StringVar()
    contra = StringVar()

    Label(pantalla1, text="Registro facial: debe de asignar un usuario:").pack()
    Label(pantalla1, text="Registro tradicional: debe asignar usuario y contraseña:").pack()
    Label(pantalla1, text="").pack()
    Label(pantalla1, text="Usuario * ").pack()
    usuario_entrada = Entry(pantalla1, textvariable=usuario)
    usuario_entrada.pack()
    Label(pantalla1, text="Contraseña * ").pack()
    contra_entrada = Entry(pantalla1, textvariable=contra, show='*')
    contra_entrada.pack()
    Label(pantalla1, text="").pack()
    Button(pantalla1, text="Registro Tradicional", width=15, height=1, command=lambda: registrar_usuario(usuario, contra)).pack()
    Label(pantalla1, text="").pack()
    Button(pantalla1, text="Registro Facial", width=15, height=1, command=lambda: None).pack()  # Implementar el registro facial aquí
