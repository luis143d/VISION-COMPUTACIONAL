from tkinter import Tk, Label, Button
from registro import registro
from login import login

def pantalla_principal():
    global pantalla
    pantalla = Tk()
    pantalla.geometry("300x250")
    pantalla.title("Aprende e Ingenia")

    Label(text="Login Inteligente", bg="gray", width="300", height="2", font=("Verdana", 13)).pack()

    Label(text="").pack()
    Button(text="Iniciar Sesion", height="2", width="30", command=lambda: login(pantalla)).pack()
    Label(text="").pack()
    Button(text="Registro", height="2", width="30", command=lambda: registro(pantalla)).pack()

    pantalla.mainloop()

if __name__ == "__main__":
    pantalla_principal()
