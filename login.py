import os
from tkinter import END, Toplevel, Label, Button, Entry, StringVar
from facial_recognition import login_facial

def verificacion_login(verificacion_usuario, verificacion_contra, pantalla2):
    log_usuario = verificacion_usuario.get()
    log_contra = verificacion_contra.get()

    usuario_entrada2.delete(0, END)
    contra_entrada2.delete(0, END)

    lista_archivos = os.listdir("users")
    if f"{log_usuario}.txt" in lista_archivos:
        with open(f"users/{log_usuario}.txt", "r") as archivo2:
            verificacion = archivo2.read().splitlines()
            if log_contra == verificacion[1]:  # Compara con la contraseña
                Label(pantalla2, text="Inicio de Sesion Exitoso", fg="green", font=("Calibri", 11)).pack()
            else:
                Label(pantalla2, text="Contraseña Incorrecta", fg="red", font=("Calibri", 11)).pack()
    else:
        Label(pantalla2, text="Usuario no encontrado", fg="red", font=("Calibri", 11)).pack()

def login(pantalla):
    global pantalla2, verificacion_usuario, verificacion_contra, usuario_entrada2, contra_entrada2
    pantalla2 = Toplevel(pantalla)
    pantalla2.title("Login")
    pantalla2.geometry("300x250")

    Label(pantalla2, text="Login facial: debe de asignar un usuario:").pack()
    Label(pantalla2, text="Login tradicional: debe asignar usuario y contraseña:").pack()
    Label(pantalla2, text="").pack()

    verificacion_usuario = StringVar()
    verificacion_contra = StringVar()

    Label(pantalla2, text="Usuario * ").pack()
    usuario_entrada2 = Entry(pantalla2, textvariable=verificacion_usuario)
    usuario_entrada2.pack()
    Label(pantalla2, text="Contraseña * ").pack()
    contra_entrada2 = Entry(pantalla2, textvariable=verificacion_contra, show='*')
    contra_entrada2.pack()
    Label(pantalla2, text="").pack()
    
    Button(pantalla2, text="Inicio de Sesion Tradicional", width=20, height=1, 
           command=lambda: verificacion_login(verificacion_usuario, verificacion_contra, pantalla2)).pack()
    Label(pantalla2, text="").pack()
    
    Button(pantalla2, text="Inicio de Sesion Facial", width=20, height=1, 
           command=lambda: login_facial(verificacion_usuario)).pack()
