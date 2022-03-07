#Librerias
from tkinter import filedialog, Tk, Label, Button, Entry, Menu, Text, Menubutton


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

    

    

################################################################
################################################################



#[ Venta Inicio ]
ventana = Tk()
ventana.geometry("800x580")
ventana.title("LFP_PY1_201906795.py")


lbl = Label(ventana,text="Cargar Archivo LFP")
lbl.pack()
lbl.place(x=10,y=20,width=100, height=30)


btnsubir = Button(ventana,text="Subir archivo", command=mensaje, padx= 20, pady = 10, fg="black", bg="#B5C7F2")
btnsubir.pack()
btnsubir.place(x=10,y=50,width=100, height=30)


width1 = 600
height1 = 400
cuadrotexto = Text(ventana, width= width1, height=height1)
cuadrotexto.pack(side="left")
cuadrotexto.place(x= 10, y=100, width = width1, height=height1)




btnanalizar = Button(ventana,text="Analizar", command=mensaje, padx= 20, pady = 10, fg="black", bg="#BBF3C5")
btnanalizar.pack()
btnanalizar.place(x=250,y=510,width=100, height=30)


btnmenu = Menubutton(ventana, text = "Menu Reportes", bg= "#F3D997",  activebackground="#DBB77D")
    
btnmenu.menu = Menu(btnmenu, tearoff=False)  
btnmenu["menu"]= btnmenu.menu  
btnmenu.menu.add_checkbutton(label = "Reporte de Tokens ",
                                variable = 2)  
btnmenu.menu.add_checkbutton(label = "Reporte de Errores",
                                variable = 2)
btnmenu.menu.add_checkbutton(label = "Manual de Usuario",
                                variable = 3)
btnmenu.menu.add_checkbutton(label = "Manual Tecnico",
                                variable = 4)                            

btnmenu.pack(expand=True)
btnmenu.place(x=650,y=140,width=100, height=30)

ventana.mainloop()

################################################################
################################################################