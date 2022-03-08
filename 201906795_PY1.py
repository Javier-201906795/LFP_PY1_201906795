#Librerias
# from tkinter import filedialog, Tk, Label, Button, Entry, Menu, Text, Menubutton, PhotoImage, font
from tkinter import *
from tkinter import filedialog, font

from Errores import Errores

#[ VARIABLES GLOBALES ]

Textform = "N/A"
TextVacioVentana = ""
ListaErrores = []



################################################################
#Test
def mensaje():
    print("mensaje")
    ventana = Tk()
    ventana.geometry("400x280")
    ventana.title("LFP_PY1_201906795.py[2]")
    
    lbl = Label(ventana,text="Ingresar un archivo")
    lbl.pack()

################################################################
def imprimirerrores():
    print("\n")
    for c in ListaErrores:
        print(c.imprimir())

################################################################
def nuevoerror(codigo,funcion,mesajee,excepccion):
    #Crea nuevo error
    newerror = Errores(codigo,funcion,mesajee,excepccion)
    #Guarda el nuevo error
    global ListaErrores
    ListaErrores.append(newerror)



################################################################
def abrirarchivoform():
    try:
        archivo = filedialog.askopenfilename(
        title = "Selecciona un archivo",
        #accede a la carpeta donde esta el archivo 
        initialdir =  "./",
        #tipo de archivo que puede seleccionar
        filetype = [
            ("Archivos LFP", "*.form"),
            ("Todos los archivos", "*.*")
        ]
        )

        #Archivo Vacio
        if archivo is None:
            print("No se selecciono ningun archivo" + "\n")
            return None
        else:
            #Abre el archivo
            with open(archivo, 'r', encoding='utf8') as file:
                text = file.read()
                file.close()
            #Imprime consola
            print("\n----------------- [ .form ] ------------------------")
            print(text)
            print("------------------------------------------------ \n")
            #Limpiar texto en Ventana
            cuadrotexto.delete('1.0', END)

            #Salvar texto en Ventana
            cuadrotexto.insert(INSERT,str(text))

            #Salvar texto en Variable
            global Textform
            Textform = str(text)

            return text
    
    except IndexError as e:
        mensajeer = "Error al cargar el archivo .form"
        nuevoerror("B01", "abrirarchivoform()",mensajeer,e)
        print("Error al abrir el archivo")

    

################################################################
def analizar():
    #Obtener Texto
    txt = str(cuadrotexto.get("1.0",END))
    #Quita el salto de linea
    txt = txt[0:len(txt) - 1]
    #Verificar si existe texto 
    errorvacio = False
    if len(txt) < 4:
        if txt == TextVacioVentana or  txt == "" or txt == " " or txt == "  " or txt == "   " or txt == "    " or txt == None:
            errorvacio = True
            texte = "El texto a analizar esta Vacio"
            nuevoerror("A01","analizar()",texte,"0")
            imprimirerrores()
    #[ ANALIZAR ]
    if errorvacio == False:
        #Convertir texto a minusculas
        txt = txt.lower()
        print(txt)
        #Encontrar la siguente cadena de caracteres "formulario"
        temp = txt.split('formulario')
        print("----- tmp")
        print(temp)
        print("-----")

        cont= 0
        for c in temp:
            cont +=1
            print("----- for ", cont)
            print(c)
        



        # contenido = txt.split("¿")[1].split("?")[0]
        # print(contenido)

################################################################
#Mensaje Bienvenida
def Iniciomensaje():
    print(" Proyecto 1 ")
    print(" 201906795 | Javier Yllescas")

################################################################
################################################################
if __name__ == "__main__":

    #[ Mensaje Consola ]
    Iniciomensaje()

    #[Imprimir Errores]
    imprimirerrores()

    

################################################################
################################################################



#[ Venta Inicio ]
ventana = Tk()
ventana.geometry("800x580")
ventana.title("LFP_PY1_201906795.py")
ventana.config(background = "white")

#Fuentes
Font1 = font.Font(family='Helvetica', size=12, weight='bold')
Font2 = font.Font(family='Helvetica', size=10, weight='bold')



lbl = Label(ventana,text="Cargar Archivo LFP", bg="white", fg="#4C5261")
lbl['font']= Font1
lbl.pack()
lbl.place(x=5,y=10,width=200, height=40)


btnsubir = Button(ventana,text="Subir archivo", command=abrirarchivoform, fg="#2C2F38", bg="#B5C7F2")
btnsubir['font']= Font2
btnsubir.pack()
btnsubir.place(x=30,y=50,width=120, height=30)


width1 = 600
height1 = 400
cuadrotexto = Text(ventana, width= width1, height=height1, bg="#D8E0F5", fg="#4C5261")
cuadrotexto.pack(side="left")
cuadrotexto.place(x= 30, y=100, width = width1, height=height1)
#Limpiar texto en Ventana
cuadrotexto.delete('1.0', END)
TextVacioVentana = cuadrotexto.get("1.0",END)


btnanalizar = Button(ventana,text="Analizar", command=analizar, padx= 20, pady = 10, fg="#2C2F38", bg="#73A775")
btnanalizar['font']= Font2
btnanalizar.pack()
btnanalizar.place(x=280,y=510,width=100, height=30)


btnmenu = Menubutton(ventana, text = "Menu Reportes", bg= "#F3D997" ,fg="#2C2F38",  activebackground="#A89972")
btnmenu['font']= Font2    
btnmenu.menu = Menu(btnmenu, tearoff=False)  
btnmenu["menu"]= btnmenu.menu  

btnmenu.menu.add_checkbutton(label = "Reporte de Tokens ", variable = 1, command=mensaje)  
btnmenu.menu.add_checkbutton(label = "Reporte de Errores", variable = 2, command=mensaje)
btnmenu.menu.add_checkbutton(label = "Manual de Usuario",  variable = 3, command=mensaje)
btnmenu.menu.add_checkbutton(label = "Manual Tecnico",     variable = 4, command=mensaje)                            

btnmenu.pack(expand=True)
btnmenu.place(x=640,y=140,width=150, height=40)

ventana.mainloop()

################################################################
################################################################



