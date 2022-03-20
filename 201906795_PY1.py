#Librerias
# from tkinter import filedialog, Tk, Label, Button, Entry, Menu, Text, Menubutton, PhotoImage, font
from calendar import c
from tkinter import *
from tkinter import filedialog, font

#my Clases
from Errores import Errores
from Elementos import Elementos

#[ VARIABLES GLOBALES ]

Textform = "N/A"
TextVacioVentana = ""
ListaErrores = []
#Elementos en Texto
ListadoElementos1 = []
#Elementos dentro de una clase para facilitar su obtencion de datos
ListadoElementos2 = []
#ListaVariablesGet para el formulario
Listadovarget = []



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
    
    except Exception as e:
        mensajeer = "Error al cargar el archivo .form"
        nuevoerror("B01", "abrirarchivoform()",mensajeer,e)
        print("Error al abrir el archivo")
        imprimirerrores()


    

################################################################
def imprimirelementos():
    print("°°°°°°°[ Elementos Lista1 - Texto ] °°°°°°°°")
    for g in ListadoElementos1:
        print(g)
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n")
    print("°°°°°°°[ Elementos Lista2 - Segmentados ] °°°°°°°°")
    for h in ListadoElementos2:
        print(h.imprimir())
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n")

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
                        nuevoerror("A04","analizar()",mensajee,"0")
                    else:
                        #B1.3 imprimir
                        print("----- [ Inicio Formulario ] ------") 
                        print(newtext)
                        print("---------------------------------")
                except Exception as e:
                    mensajee = "Error al buscar la palabra clave 'formulario~>>'"
                    nuevoerror("A05","analizar()",mensajee,e)

                #B1.4 Guardar Texto
                if newtext == " " or newtext == "":
                    textolimpio = textosinespacios
                else:
                    textolimpio = newtext
            ################################################################
            #[C1.0 Encontrar "[<"]
            if (val2):
                newtext = ''
                try:
                    largotextoabuscar = 2
                    for g in range(0,len(textolimpio)-largotextoabuscar):
                        #C1.1 texto a evaluar
                        textoAevaluar = textolimpio[g:g+largotextoabuscar]
                        #C1.2 Encontrar texto
                        if textoAevaluar == "[<": 
                            newtext = textolimpio[g+largotextoabuscar:len(textolimpio)]
                            break
                    
                    # print("newTEXT:",newtext)
                    #C1.1.1 No se encontro el texto a buscar
                    if(newtext == "" or newtext == " "):
                        mensajee = "No se puedo obtener el inicio del formulario. (No se encontro la palabra clave '[<'"
                        nuevoerror("A04.1","analizar()",mensajee,"0")
                except Exception as e:
                    mensajee = "Error al buscar la palabra clave '[<'"
                    nuevoerror("A06","analizar()",mensajee,e)
            ################################################################
            #[D1.0 Encontrar Elementos "<" y ">"]
            if (val2):
                val3=True
                
                try:
                    while(True):
                        inicio = -1
                        fin = -1
                        #Encontrar "<"
                        newtext = ''
                        textoabuscar1 = "<t"
                        cont = -1
                        for g in range(0,len(textolimpio)-len(textoabuscar1)):
                            cont +=1
                            #1.1 texto a evaluar
                            textoAevaluar = textolimpio[g:g+len(textoabuscar1)]
                            #1.2 Encontrar texto
                            if textoAevaluar == textoabuscar1: 
                                #1.2.1 Guardar posicion
                                inicio = cont
                                break
                        

                        #e1.1.1 No se encontro el texto a buscar salir de bucle
                        if(inicio == -1 ):
                            val3= False
                            break

                        ####################
                        #2.1 Encontrar ">"
                        textoabuscar1 = ">,"
                        textoabuscar2 = ">]"
                        if(val3):
                            cont2 = 0
                            for g in range(0,len(textolimpio)-(len(textoabuscar1)-1)):
                                cont2 +=1
                                #2.1 texto a evaluar
                                textoAevaluar = textolimpio[g:g+len(textoabuscar1)]
                                # print("texto a evaluar:",textoAevaluar)
                                #2.2 Encontrar texto
                                if textoAevaluar == textoabuscar1 or textoAevaluar == textoabuscar2:
                                    #2.2.1 Guardar posicion 
                                    fin = cont2
                                    break

                        #e2.1.1 No se encontro el texto a buscar
                        if(fin == -1):
                            mensajee = "No se encontro la palabra clave: '" + str(textoabuscar1) + "'."
                            nuevoerror("A07.1","analizar()",mensajee,"0")
                            val3 = False
                            val2 = False
                        else:
                            #3.5 Guardar Elemento
                            nuevoelemento = textolimpio[inicio + 1:fin - 1]
                            global ListadoElementos1
                            ListadoElementos1.append(nuevoelemento)

                        
                        #[No quitar BUG1] 4.1 Nuevo Texto 
                        textolimpio = textolimpio[fin:len(textolimpio)]
                    #[No quitar BUG1] 4.1.1Imprimir Texto
                    print(textolimpio)
                        

                except Exception as e:
                    mensajee = "Error al buscar la palabra clave: '" + str(textoabuscar1) + "'."
                    nuevoerror("A07","analizar()",mensajee,e)
                    val2 = False
            
            ################################################################
            #[F Segmentar Elementos]
            #F 0.1 Valuar si hay elementos a evaluar
            if len(ListadoElementos1) > 1:
                for elemento in ListadoElementos1:
                    #[ F 0.2 CREAR ELEMETNO ]
                    newelemento = Elementos()

                    ##########################
                    ##########################
                    # [F1.1 -- TIPO -- ]
                    val4=True
                    inicio = -1
                    fin = -1
                    newtext = ''
                    textoabuscar1 = 'tipo:"'
                    textoabuscar2 = "tipo:'"
                    cont = -1
                    for g in range(0,len(elemento)-len(textoabuscar1)):
                        cont +=1
                        #1.1 texto a evaluar
                        textoAevaluar = elemento[g:g+len(textoabuscar1)]
                        # print(cont, " - ", textoAevaluar)
                        #1.2 Encontrar texto
                        if textoAevaluar == textoabuscar1 or textoAevaluar == textoabuscar2: 
                            #1.2.1 Guardar posicion
                            inicio = cont + len(textoabuscar1)
                            break
                    
                    #e1.1.1 No se encontro el texto a buscar salir de bucle
                    if(inicio == -1 ):
                        mensajee = "Error al buscar la palabra clave: '" + str(textoabuscar1) + "', porfavor ingrese un tipo de elemento."
                        nuevoerror("A07.2","analizar()",mensajee,"0")
                        val4 = False

                    ########
                    #2.1 Encontrar 
                    textoabuscar1 = "',"
                    textoabuscar2 = '",'
                    if(val4):
                        cont2 = 0
                        for g in range(0,len(elemento)-(len(textoabuscar1)-1)):
                            cont2 +=1
                            #2.1 texto a evaluar
                            textoAevaluar = elemento[g:g+len(textoabuscar1)]
                            # print(cont, " - ", textoAevaluar)
                            #2.2 Encontrar texto
                            if textoAevaluar == textoabuscar1 or textoAevaluar == textoabuscar2:
                                #2.2.1 Guardar posicion 
                                fin = cont2 - 1
                                break  

                        #e2.1.1 No se encontro el texto a buscar
                        if(fin == -1):
                            mensajee = "No se encontro la palabra clave: '" + str(textoabuscar1) + "'."
                            nuevoerror("A07.2","analizar()",mensajee,"0")
                            val3 = False
                            val2 = False
                        else:
                            try:
                                Gtipo = elemento[inicio:fin]
                                #[ 3.5 GUARDAR TIPO ]
                                newelemento.settipo(Gtipo)
                                #[ 4.0 Guardar Nuevo Elemento (Texto Lista1)]
                                elemento = elemento[fin+2:len(elemento)]
                            except Exception as e:
                                texte = "Error al guardar tipo."
                                nuevoerror("A07","analizar()",texte,e)

                    #########################
                    #########################
                    # [G1.1 -- Valor -- ]
                    try:
                        # print(">-----[Texto a evaluar]---" )
                        # print(elemento)
                        # print(">-------------------------")

                        val4=True
                        inicio = -1
                        fin = -1
                        newtext = ''
                        textoabuscar1 = 'valor:"'
                        textoabuscar2 = "valor:'"
                        cont = -1
                        for g in range(0,len(elemento)-len(textoabuscar1)):
                            cont +=1
                            #1.1 texto a evaluar
                            textoAevaluar = elemento[g:g+len(textoabuscar1)]
                            # print(cont, " - ", textoAevaluar)
                            #1.2 Encontrar texto
                            if textoAevaluar == textoabuscar1 or textoAevaluar == textoabuscar2: 
                                #1.2.1 Guardar posicion
                                inicio = cont + len(textoabuscar1)
                                break
                        

                        #e1.1.1 No se encontro el texto No tiene "valor"
                        if(inicio == -1 ):
                            val4 = False
                        else:
                            # Guardar Elemento solo comillas
                            temptext = elemento[inicio:len(elemento)]
                            # print(">>--- [Nuevo Texto] --")
                            # print(temptext)
                            # print(">>-----")

                        ########
                        #2.1 Encontrar 
                        textoabuscar1 = "'"
                        textoabuscar2 = '"'
                        if(val4):
                            cont2 = 0
                            for g in range(0,len(temptext)):
                                cont2 +=1
                                #2.1 texto a evaluar
                                textoAevaluar = temptext[g:g+len(textoabuscar1)]
                                # print(cont2, " - ", textoAevaluar)
                                #2.2 Encontrar texto
                                if textoAevaluar == textoabuscar1 or textoAevaluar == textoabuscar2:
                                    #2.2.1 Guardar posicion 
                                    fin = cont2 
                                    break  
                                    
                            

                            #e2.1.1 No se encontro el texto a buscar
                            if(fin == -1):
                                mensajee = "No se encontro la palabra clave: '" + str(textoabuscar1) + "'."
                                nuevoerror("A09.2","analizar()",mensajee,"0")
                            else:
                                try:
                                    fin = fin + inicio -1
                                    Gvalor = elemento[inicio:fin]
                                    # print(Gvalor)
                                    #[ 3.5 GUARDAR VALOR ]
                                    newelemento.setvalor(Gvalor)
                                    # print(">>>----[ Resultado ]----")
                                    # print(newelemento.valor)
                                    # print(">>>---------------------")
                                    #[ 4.0 Guardar Nuevo Elemento (Texto Lista1)]
                                    elemento = elemento[fin+2:len(elemento)]
                                    # print(elemento)
                                except Exception as e:
                                    texte = "Error al guardar tipo."
                                    nuevoerror("A09.1","analizar()",texte,e)
                    except Exception as e:
                        texte = "Error al encontrar valor."
                        nuevoerror("A09","analizar()",texte,e)

                    #########################
                    #########################
                    # [G1.1 -- Fondo -- ]
                    try:
                        # print(">-----[Texto a evaluar]---" )
                        # print(elemento)
                        # print(">-------------------------")

                        val4=True
                        inicio = -1
                        fin = -1
                        newtext = ''
                        textoabuscar1 = 'fondo:"'
                        textoabuscar2 = "fondo:'"
                        cont = -1
                        for g in range(0,len(elemento)-len(textoabuscar1)):
                            cont +=1
                            #1.1 texto a evaluar
                            textoAevaluar = elemento[g:g+len(textoabuscar1)]
                            # print(cont, " - ", textoAevaluar)
                            #1.2 Encontrar texto
                            if textoAevaluar == textoabuscar1 or textoAevaluar == textoabuscar2: 
                                #1.2.1 Guardar posicion
                                inicio = cont + len(textoabuscar1)
                                break
                        

                        #e1.1.1 No se encontro el texto No tiene "valor"
                        if(inicio == -1 ):
                            val4 = False
                        else:
                            # Guardar Elemento solo comillas
                            temptext = elemento[inicio:len(elemento)]
                            # print(">>--- [Nuevo Texto] --")
                            # print(temptext)
                            # print(">>-----")

                        ########
                        #2.1 Encontrar 
                        textoabuscar1 = "'"
                        textoabuscar2 = '"'
                        if(val4):
                            cont2 = 0
                            for g in range(0,len(temptext)):
                                cont2 +=1
                                #2.1 texto a evaluar
                                textoAevaluar = temptext[g:g+len(textoabuscar1)]
                                # print(cont2, " - ", textoAevaluar)
                                #2.2 Encontrar texto
                                if textoAevaluar == textoabuscar1 or textoAevaluar == textoabuscar2:
                                    #2.2.1 Guardar posicion 
                                    fin = cont2 
                                    break  
                                    
                            

                            #e2.1.1 No se encontro el texto a buscar
                            if(fin == -1):
                                mensajee = "No se encontro la palabra clave: '" + str(textoabuscar1) + "'."
                                nuevoerror("A10.2","analizar()",mensajee,"0")
                            else:
                                try:
                                    fin = fin + inicio -1
                                    Gfondo = elemento[inicio:fin]
                                    # print(Gvalor)
                                    #[ 3.5 GUARDAR VALOR ]
                                    newelemento.setfondo(Gfondo)
                                    # print(">>>----[ Resultado ]----")
                                    # print(newelemento.valor)
                                    # print(">>>---------------------")
                                    #[ 4.0 Guardar Nuevo Elemento (Texto Lista1)]
                                    elemento = elemento[fin+2:len(elemento)]
                                    # print(elemento)
                                except Exception as e:
                                    texte = "Error al guardar Fondo."
                                    nuevoerror("A10.1","analizar()",texte,e)
                    except Exception as e:
                        texte = "Error al encontrar fondo."
                        nuevoerror("A10","analizar()",texte,e)

                    #########################
                    #########################
                    # [H1.1 -- Nombre -- ]
                    try:
                        # print(">-----[Texto a evaluar]---" )
                        # print(elemento)
                        # print(">-------------------------")

                        val4=True
                        inicio = -1
                        fin = -1
                        newtext = ''
                        textoabuscar1 = 'nombre:"'
                        textoabuscar2 = "nombre:'"
                        cont = -1
                        for g in range(0,len(elemento)-len(textoabuscar1)):
                            cont +=1
                            #1.1 texto a evaluar
                            textoAevaluar = elemento[g:g+len(textoabuscar1)]
                            # print(cont, " - ", textoAevaluar)
                            #1.2 Encontrar texto
                            if textoAevaluar == textoabuscar1 or textoAevaluar == textoabuscar2: 
                                #1.2.1 Guardar posicion
                                inicio = cont + len(textoabuscar1)
                                break
                        

                        #e1.1.1 No se encontro el texto No tiene "valor"
                        if(inicio == -1 ):
                            val4 = False
                        else:
                            # Guardar Elemento solo comillas
                            temptext = elemento[inicio:len(elemento)]
                            # print(">>--- [Nuevo Texto] --")
                            # print(temptext)
                            # print(">>-----")

                        ########
                        #2.1 Encontrar 
                        textoabuscar1 = "'"
                        textoabuscar2 = '"'
                        if(val4):
                            cont2 = 0
                            for g in range(0,len(temptext)):
                                cont2 +=1
                                #2.1 texto a evaluar
                                textoAevaluar = temptext[g:g+len(textoabuscar1)]
                                # print(cont2, " - ", textoAevaluar)
                                #2.2 Encontrar texto
                                if textoAevaluar == textoabuscar1 or textoAevaluar == textoabuscar2:
                                    #2.2.1 Guardar posicion 
                                    fin = cont2 
                                    break  
                                    
                            

                            #e2.1.1 No se encontro el texto a buscar
                            if(fin == -1):
                                mensajee = "No se encontro la palabra clave: '" + str(textoabuscar1) + "'."
                                nuevoerror("A11.2","analizar()",mensajee,"0")
                            else:
                                try:
                                    fin = fin + inicio -1
                                    Gnombre = elemento[inicio:fin]
                                    # print(Gnombre)
                                    #[ 3.5 GUARDAR VALOR ]
                                    newelemento.setnombre(Gnombre)
                                    # print(">>>----[ Resultado ]----")
                                    # print(newelemento.valor)
                                    # print(">>>---------------------")
                                    #[ 4.0 Guardar Nuevo Elemento (Texto Lista1)]
                                    elemento = elemento[fin+2:len(elemento)]
                                    # print(elemento)
                                except Exception as e:
                                    texte = "Error al guardar Nombre."
                                    nuevoerror("A11.1","analizar()",texte,e)
                    except Exception as e:
                        texte = "Error al encontrar nombre."
                        nuevoerror("A11","analizar()",texte,e)

                    #########################
                    #########################
                    # [J1.1 -- evento -- ]
                    try:
                        # print(">-----[Texto a evaluar]---" )
                        # print(elemento)
                        # print(">-------------------------")

                        val4=True
                        inicio = -1
                        fin = -1
                        newtext = ''
                        textoabuscar1 = 'evento:<'
                        textoabuscar2 = "evento:<"
                        cont = -1
                        for g in range(0,len(elemento)-len(textoabuscar1)):
                            cont +=1
                            #1.1 texto a evaluar
                            textoAevaluar = elemento[g:g+len(textoabuscar1)]
                            # print(cont, " - ", textoAevaluar)
                            #1.2 Encontrar texto
                            if textoAevaluar == textoabuscar1 or textoAevaluar == textoabuscar2: 
                                #1.2.1 Guardar posicion
                                inicio = cont + len(textoabuscar1)
                                break
                        

                        #e1.1.1 No se encontro el texto No tiene "valor"
                        if(inicio == -1 ):
                            val4 = False
                        else:
                            # Guardar Elemento solo comillas
                            temptext = elemento[inicio:len(elemento)]
                            # print(">>--- [Nuevo Texto] --")
                            # print(temptext)
                            # print(">>-----")

                        ########
                        #2.1 Encontrar 
                        textoabuscar1 = ">"
                        textoabuscar2 = '>'
                        if(val4):
                            cont2 = 0
                            for g in range(0,len(temptext)):
                                cont2 +=1
                                #2.1 texto a evaluar
                                textoAevaluar = temptext[g:g+len(textoabuscar1)]
                                # print(cont2, " - ", textoAevaluar)
                                #2.2 Encontrar texto
                                if textoAevaluar == textoabuscar1 or textoAevaluar == textoabuscar2:
                                    #2.2.1 Guardar posicion 
                                    fin = cont2 
                                    break  
                                    
                            

                            #e2.1.1 No se encontro el texto a buscar
                            if(fin == -1):
                                mensajee = "No se encontro la palabra clave: '" + str(textoabuscar1) + "'."
                                nuevoerror("A12.2","analizar()",mensajee,"0")
                            else:
                                try:
                                    fin = fin + inicio -1
                                    Gevento = elemento[inicio:fin]
                                    # print(Gnombre)
                                    #[ 3.5 GUARDAR VALOR ]
                                    newelemento.setevento(Gevento)
                                    # print(">>>----[ Resultado ]----")
                                    # print(newelemento.valor)
                                    # print(">>>---------------------")
                                    #[ 4.0 Guardar Nuevo Elemento (Texto Lista1)]
                                    elemento = elemento[fin+2:len(elemento)]
                                    # print(elemento)
                                except Exception as e:
                                    texte = "Error al guardar evento."
                                    nuevoerror("A12.1","analizar()",texte,e)
                    except Exception as e:
                        texte = "Error al encontrar evento."
                        nuevoerror("A12","analizar()",texte,e)
                    
                    #########################
                    #########################
                    # [K1.1 -- valores -- ]
                    try:
                        # print(">-----[Texto a evaluar]---" )
                        # print(elemento)
                        # print(">-------------------------")

                        val4=True
                        inicio = -1
                        fin = -1
                        newtext = ''
                        textoabuscar1 = 'valores:['
                        textoabuscar2 = "valores:{"
                        cont = -1
                        for g in range(0,len(elemento)-len(textoabuscar1)):
                            cont +=1
                            #1.1 texto a evaluar
                            textoAevaluar = elemento[g:g+len(textoabuscar1)]
                            # print(cont, " - ", textoAevaluar)
                            #1.2 Encontrar texto
                            if textoAevaluar == textoabuscar1 or textoAevaluar == textoabuscar2: 
                                #1.2.1 Guardar posicion
                                inicio = cont + len(textoabuscar1)
                                break
                        
                        
                        
                        #e1.1.1 No se encontro el texto No tiene "valor"
                        if(inicio == -1 ):
                            val4 = False
                        else:
                            # Guardar Elemento solo comillas
                            temptext = elemento[inicio:len(elemento)]
                            # print(">>--- [Nuevo Texto] --")
                            # print(temptext)
                            # print(">>-----")

                        ########
                        #2.1 Encontrar 
                        textoabuscar1 = "]"
                        textoabuscar2 = '}'
                        if(val4):
                            cont2 = 0
                            for g in range(0,len(temptext)):
                                cont2 +=1
                                #2.1 texto a evaluar
                                textoAevaluar = temptext[g:g+len(textoabuscar1)]
                                # print(cont2, " - ", textoAevaluar)
                                #2.2 Encontrar texto
                                if textoAevaluar == textoabuscar1 or textoAevaluar == textoabuscar2:
                                    #2.2.1 Guardar posicion 
                                    fin = cont2 
                                    break  
                                    
                            

                            #e2.1.1 No se encontro el texto a buscar
                            if(fin == -1):
                                mensajee = "No se encontro la palabra clave: '" + str(textoabuscar1) + "'."
                                nuevoerror("A13.2","analizar()",mensajee,"0")
                            else:
                                try:
                                    fin = fin + inicio -1
                                    Gvalores = elemento[inicio:fin]
                                    #[3.0 Procesar valores]
                                    Tvalores = Gvalores
                                    cont =0
                                    #3.0.1 Convertir texto a una lista
                                    Listavalores = []
                                    try:
                                        #3.0.2 Evaluar texto
                                        for j in Gvalores:
                                            inicio2 = -1
                                            fin2 = -1
                                            newtext = ''
                                            textoabuscar1 = ','
                                            textoabuscar2 = ","
                                            cont = -1
                                            for g in range(0,len(Tvalores)-len(textoabuscar1)):
                                                cont +=1
                                                #3.1 texto a evaluar
                                                textoAevaluar = Tvalores[g:g+len(textoabuscar1)]
                                                # print(cont, " - ", textoAevaluar)
                                                #3.2 Encontrar texto
                                                if textoAevaluar == textoabuscar1 or textoAevaluar == textoabuscar2: 
                                                    #3.2.1 Guardar posicion
                                                    fin2 = cont + len(textoabuscar1) - 1
                                                    break

                                            #valor 1
                                            elementovalor = Tvalores[0:fin2]
                                            
                                            #3.3 quitar valor encontrado
                                            fin2 = fin2 + 1
                                            Tvalores = Tvalores[fin2:len(Tvalores)]
                                            
                                            

                                            # print("R:",elementovalor)
                                            # print("Tvalores:",Tvalores)
                                            # print("fin2:",fin2)

                                            #3.4.1 Fin del bucle Listado
                                            #si no encuentra ,
                                            if (fin2 == 0):
                                                #3.4.1 ultimo valor diferente por la comilla al final
                                                elementovalor = Tvalores[0:len(Tvalores)]
                                                # print("elementovalor",elementovalor)
                                                #3.4.2 Guardar en listado
                                                Listavalores.append(elementovalor)
                                                break

                                            #3.4.0 Guardar en listado
                                            Listavalores.append(elementovalor)

                                            

                                    except Exception as e:
                                        texte = "Error al crear listado con los valores."
                                        nuevoerror("A13.3","analizar()",texte,e)

                                    #[ 3.5 GUARDAR VALORES ]

                                    #Imprimir listado valores
                                    # for g in Listavalores:
                                    #     print(g)

                                    newelemento.setvalores(Listavalores)
                                    # print(">>>----[ Resultado ]----")
                                    # print(newelemento.valores)
                                    # listatemp = newelemento.valores
                                    # for h in listatemp:
                                    #     print(h)
                                    # print(listatemp[1])
                                    # print(">>>---------------------")
                                    #[ 4.0 Guardar Nuevo Elemento (Texto Lista1)]
                                    elemento = elemento[fin+2:len(elemento)]
                                    # print(elemento)
                                except Exception as e:
                                    texte = "Error al guardar valores."
                                    nuevoerror("A13.1","analizar()",texte,e)
                    except Exception as e:
                        texte = "Error al encontrar valores."
                        nuevoerror("A13.1","analizar()",texte,e)

                    ############################
                    ############################
                    print("##### [ Elemento a Evaluar ] ####")
                    print(elemento)
                    
                    ############################
                    ############################
                    #[ GUARDAR ELEMENTOS EN LISTADO 2 ]
                    global ListadoElementos2
                    ListadoElementos2.append(newelemento)
                    ############################
                    ############################

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
        
        # [X1.0Imprimir Elementos]
        imprimirelementos()

        # [Z1.0 IMPRIMIR ERRORES ]
        imprimirerrores()

        # [Z2.0 CREAR FORMULARIO]
        if len(ListadoElementos2) > 0:
            crearformulario()



################################################################
#/////////////////////////////////////////////////////////////////
#Funcion para crear labels
def Flabel(Valor):
    contenido = """//----------------------------------------------------------------
//[L1.0 LABEL ]
contenidoform = '<label class="mb-3">"""+ str(Valor) +"""</label>'"""

    contenido +="""         
        
"""
    return contenido
#/////////////////////////////////////////////////////////////////
#Funcion para crear INPUT TEXT
def Finputtext(Valor, Fondo):
    contenido = """//----------------------------------------------------------------
//[T1.0 TEXTO - INPUT ]
contenidoform += '<div class="input-group input-group-sm mb-4">'+
'<div class="input-group-prepend col-md-2">'+
    '<span class="input-group-text">""" + str(Valor) + """</span>'+
'</div>'+
'<div class="col-md-7">'+
    '<input type="text" class="form-control col-sm-2" aria-label="Small" placeholder=""" + '"' + str(Fondo) + '"' + """ id="""+ '"' +'inputtext'+ str(Valor) + '"' +""">'+
'</div>'+
'</div>'"""

    contenido +="""         
        
"""

    return contenido 

#/////////////////////////////////////////////////////////////////
#Funcion para crear INPUT RADIO
def Finputradio(Nombre,Valores):
    contenido ="""//----------------------------------------------------------------
//[R1.0 GRUPO RADIO - GRUPO INPUT ]
contenidoform += '<div class="col-md-12 mb-4">'+
'<div class="col-md-2 mb-0 input-group-sm">'+
    '<span class="input-group-text">"""+str(Nombre)+"""</span>'+
'</div>'+"""

    #[A 1.0 Validar si hay Elementos en la lista]
    if (len(Valores) > 0):
        cont = 0
        for g in Valores:
            cont += 1
            # 1.1 Agregar al listado de elementos radio
            contenido += """'<div class="form-check mb-0">'+
    '<input class="form-check-input" type="radio"  name="""+'"'+'inputradio'+str(Nombre)+'"'+""">'+
'<label class="form-check-label">'+
    '""" +  g  + """'+
'</label>'+
'</div>'+"""
        #2.1 Fin For cierrre del div
        contenido +="""'</div>'"""

    #Espacio
    contenido +="""         
        
"""
    #3.1 Convertir listado a texto
    txtlist = Gconvertirlistadoatexto(Valores)


    #[ 4.0 Funcion para obtener datos ]
    contenido += """//Z1.1 OBTENER INPUT - RADIO SELECCIONADO
Nombre = document.getElementsByName("""+'"'+'inputradio'+str(Nombre)+'"'+""")"""

    #Espacio
    contenido +="""         
        
"""
    #4.1 crea la funcion 
    contenido += """function obtener"""+'inputradio'+str(Nombre)+"""() {"""
    contenido += """//2.1 Listado con los Valores
    listadoNombre = """+ txtlist +"""

    //3.1 Obtiene los input radio 
    var ele = document.getElementsByName("""+'"'+'inputradio'+str(Nombre)+'"'+""");
    //3.1.1 Evalua uno por uno para encontrar con el seleccionado
    for(i = 0; i < ele.length; i++) {
        if(ele[i].checked)
        //3.1.2 Guarda su Valor
        alert(listadoNombre[i])
    }
    return listadoNombre[i]
}"""
    

    #Espacio
    contenido +="""         
        
"""
    #4.2 Guarda el nombre la funcion
    global Listadovarget
    nombreVar = "inputradio"+ str(Nombre) + "()"
    Listadovarget.append(nombreVar)

    return contenido
################################################################
#/////////////////////////////////////////////////////////////////
def Finputselect(Nombre,Valores):

    contenido = """//----------------------------------------------------------------
//[ S 1.0 GRUPO OPTION - SELECT ]
contenidoform += '<div class="input-group mb-3">'+
'<div class="input-group-prepend col-md-2">'+
    '<label class="input-group-text" >"""+ str(Nombre)+"""</label>'+
'</div>'+
'<select class="custom-select col-md-3" id="select"""+str(Nombre)+'"'+""">'+
    '<option value="0" selected>Selecciona una opcion</option>'+"""
    
    #listado Valores
    for g in Valores:
        contenido += """'<option value="Valores1">"""+ str(g) +"""</option>'+"""

    contenido += """'</select>'+
'</div>'
"""

    contenido +="""         
        
"""

    contenido += """//3.1 Obtener opcion seleccionadas
function obtenerselect"""+str(Nombre)+"""(){
    selectNombre1 = document.getElementById("select"""+str(Nombre)+'"'+""")
    return selectNombre1.value
}"""

    contenido +="""         
        
"""
    return str(contenido)

#/////////////////////////////////////////////////////////////////
################################################################
def Fboton(Valor, Evento):
    variableValor = ""
    #Quitar Espacios
    variableValor = Gquitarespacios(Valor)
    print(variableValor)

    #Evaluar que tipo de boton es entrada o info
    if (Evento == 'entrada' or Evento == 'Entrada'):
        contenido ="""//----------------------------------------------------------------
//[B 1.0 BOTON - BUTTON | ENTRADA]
contenidoform += '<div class="row ">'+
    '<button type="button" class="btn btn-primary btn-lg col-md-2 mb-4" onclick="entrada"""+str(variableValor)+"""()">"""+str(Valor)+"""</button>'+
'</div>'"""

        contenido +="""         
            
    """

        contenido +="""//3.1 Evento
    function entrada"""+str(variableValor)+"""(){
        alert("entrada")
        

    }"""

        contenido +="""         
            
    """
    else:
        contenido ="""//----------------------------------------------------------------
//[B 1.0 BOTON - BUTTON | INFO]
contenidoform += '<div class="row ">'+
    '<button type="button" class="btn btn-secondary btn-lg col-md-2 mb-4" onclick="info"""+str(variableValor)+"""()">"""+str(Valor)+"""</button>'+
'</div>'"""

        contenido +="""         
            
    """

        contenido +="""//3.1 Evento
    function info"""+str(variableValor)+"""(){
        alert("info")
        

    }"""

        contenido +="""         
            
    """
        
        

    contenido +="""         
        
"""

    return contenido

################################################################
def Gquitarespacios(Texto):
    texttemp = ""
    for g in Texto:
        #A2.2 Evaluar si es un salto de Linea
        if g == "\n" or g == "\r" or g == " ": 
            pass
        else:
            texttemp += g.lower()
    return texttemp

def Gconvertirlistadoatexto(Listado):
    #Convertir listado a texto
    txtlist = "["
    cont1 = 0
    for g in Listado:
        cont1 += 1 
        txtlist += "'" + g +"'"
        if cont1 < len(Listado):
            txtlist += ","

    txtlist += "]"

    print(txtlist)
    return str(txtlist)


#/////////////////////////////////////////////////////////////////
################################################################
def crearformulario():
    print("creando formulario...")

    #[A1.0 Crear JAVASCRIPT ] 
    try:
        #[1.2 Abre el archivo]
        f = open('formulario.js','w')
        #[2.0 Nuevo contenido]

        #DIV contenedor de formulario
        contenido = """//Obtener div donde se colocara los elementos del formulario
divcontenido = document.getElementById("contenidoformulario");"""

        #[ CREAR LABEL ]
        contenido += Flabel("mario")

        #[ CREAR INPUT TEXT ]
        contenido += Finputtext("mario","fondomario")


        #[ CREAR INPUT RADIO ]
        lista1 = ["mario1","mario2"]
        contenido += Finputradio("mario",lista1)
        
        #[ CREAR INPUT SELECT ]
        lista2 = ["mario1","mario2"]
        contenido += Finputselect("mario",lista2)

        #[ CREAR BOTON ]
        contenido += Fboton("boton mario","entrada")

        #IMPRIME NOMBRE FUNCIONES
        print(Listadovarget)
        



        contenido +="""divcontenido.innerHTML = contenidoform"""



        f.write(contenido)
        f.close()
    except Exception as e:
        print("Error al modicar archivo javascript")
        print(e)

    mensaje = "Se creo el Formulario con exito"
    return mensaje



#/////////////////////////////////////////////////////////////////
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



