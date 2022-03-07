#Librerias
from tkinter import filedialog, Tk, Label, Button, ttk

#Test
def mensaje():
    print("mensaje")
    ventana = Tk()
    ventana.geometry("400x280")
    ventana.title("LFP_PY1_201906795.py[2]")
    
    lbl = Label(ventana,text="Ingresar un archivo")
    lbl.pack()


#Mensaje Bienvenida
def Iniciomensaje():
    print(" Proyecto 1 ")
    print(" 201906795 | Javier Yllescas")

################################################################
################################################################
if __name__ == "__main__":

    #[ Mensaje Consola ]
    Iniciomensaje()

    #[ Venta Inicio ]
    ventana = Tk()
    ventana.geometry("1000x720")
    ventana.title("LFP_PY1_201906795.py")
    
    
    lbl = Label(ventana,text="Cargar Archivo LFP")
    lbl.pack()

    btn = Button(ventana,text="Subir archivo", command=mensaje, padx= 20, pady = 10, fg="black", bg="#B5C7F2" )
    btn.pack()

    ventana.mainloop()

    

################################################################