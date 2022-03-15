#Librerias
# from tkinter import filedialog, Tk, Label, Button, Entry, Menu, Text, Menubutton, PhotoImage, font
from tkinter import *
from tkinter import filedialog, font

from Errores import Errores

#[ VARIABLES GLOBALES ]

Textform = "N/A"
TextVacioVentana = ""
ListaErrores = []
ListadoElementos = []



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
    print("==============[ Errores ]==================")
    for c in ListaErrores:
        print(c.imprimir())
    print("===========================================")

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
def imprimirelementos():
    print("°°°°°°°[ Elementos ] °°°°°°°°")
    for g in ListadoElementos:
        print(g)
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n")
#/////////////////////////////////////////////////////////////////

#/////////////////////////////////////////////////////////////////

################################################################
def analizar():
    #[ VALIDADORES ]
    #Procesar texto
    val1 = True
    val2 = True


    #Obtener Texto de la Ventana
    try:
        txt = str(cuadrotexto.get("1.0",END))
    except Exception as e:
        mensajee = "No se puedo convertir a texto"
        nuevoerror("A00","analizar()",mensajee, e)
        val1 = False
    
    #Quita el salto de linea
    if (val1):
        txt = txt[0:len(txt) - 1]

    #Verificar si existe texto 
    errorvacio = False
    if len(txt) < 4:
        if txt == TextVacioVentana or  txt == "" or txt == " " or txt == "  " or txt == "   " or txt == "    " or txt == None:
            errorvacio = True
            texte = "El texto a analizar esta Vacio"
            nuevoerror("A01","analizar()",texte,"0")
            imprimirerrores()
            val1 = False
        
    #[1.0 ANALIZAR ]
    if errorvacio == False and val1 == True:
        ################################################################
        try:
            #[ A2.0 QUITAR ESPACIOS Y SALTOS DE LINEA ]
            try:
                contador= -1
                texttemp = ''
                #Banderas flag1 = Deshabilita quitar espacios
                flag1 = False
                for g in txt:
                    contador += 1
                    #A3.0 Evaluar si hay comillas (Texto importante)
                    if g == '"' or g == "'": 
                        #A3.1 deshabilitar quitar espacios
                        if flag1 == False:
                            flag1 = True
                        else:
                            flag1 = False
                        #A3.3 agrega comilla
                        texttemp += g
                    else:
                        if flag1 == False:
                            #A2.2 Evaluar si es un salto de Linea
                            if g == "\n" or g == "\r" or g == " ": 
                                pass
                            else:
                                texttemp += g.lower()
                        else:
                            #A3.2 agregar al texto con Espacios
                            texttemp += g
                    
                #A2.2 imprimir
                print("------------ [ Texto A procesar ] -------------") 
                textosinespacios = texttemp
                print(textosinespacios)
                print("-----------------------------------------------") 

            except Exception as e:
                mensajee = "Error al evaluar texto no se pudieron quitar los espacios"
                nuevoerror("A03","analizar()",mensajee,e)
                val2 = False

            ################################################################
            #[ B1.0 Obtener Inicio Formulario "formulario~>>" ]
            if (val2):
                try:
                    newtext = ''
                    for g in range(0,len(textosinespacios)-13):
                        #B1.1 texto a evaluar
                        textoAevaluar = textosinespacios[g:g+13]
                        #B1.2 Encontrar texto
                        if textoAevaluar == "formulario~>>": 
                            newtext = textosinespacios[g+13:len(textosinespacios)]
                            break
                    #B1.1.1 No se encontro el texto a buscar
                    if(newtext == "" or newtext == " "):
                        mensajee = "No se puedo obtener el inicio del formulario. (No se encontro la palabra clave 'formulario~>>'"
                        nuevoerror("A04","analizar()",mensajee,e)
                    else:
                        #B1.3 imprimir
                        print("----- [ Inicio Formulario ] ------") 
                        print(newtext)
                        print("---------------------------------")
                except Exception as e:
                    mensajee = "Error al buscar la palabra clave 'formulario~>>'"
                    nuevoerror("A05","analizar()",mensajee,e)
            ################################################################
        except Exception as e:
            texte = "Error al analizar texto."
            nuevoerror("A02","analizar()",texte,e)

        # #GUARDAR ELEMENTOS
        # global ListadoElementos
        # for h in list7:
        #     ListadoElementos.append(h)
        # #Imprimir Elementos Guardados
        # imprimirelementos()
        

        # [Z1.0 IMPRIMIR ERRORES ]
        imprimirerrores()

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



