//Obtener div donde se colocara los elementos del formulario
divcontenido = document.getElementById("contenidoformulario");//----------------------------------------------------------------
//[L1.0 LABEL ]
contenidoform = '<label class="mb-3">Nombre:</label>'         
        
//----------------------------------------------------------------
//[T1.0 TEXTO - INPUT ]
contenidoform += '<div class="input-group input-group-sm mb-4">'+
'<div class="input-group-prepend col-md-2">'+
    '<span class="input-group-text">Nombre</span>'+
'</div>'+
'<div class="col-md-7">'+
    '<input type="text" class="form-control col-sm-2" aria-label="Small" placeholder="Ingrese nombre" id="inputtextnombre">'+
'</div>'+
'</div>'         
        
function obtenerinputtextnombre(){
        inputE = document.getElementById("inputtextnombre")
        return inputE.value
    }         
        
//----------------------------------------------------------------
//[R1.0 GRUPO RADIO - GRUPO INPUT ]
contenidoform += '<div class="col-md-12 mb-4">'+
'<div class="col-md-2 mb-0 input-group-sm">'+
    '<span class="input-group-text">sexo</span>'+
'</div>'+'<div class="form-check mb-0">'+
    '<input class="form-check-input" type="radio"  name="inputradiosexo">'+
'<label class="form-check-label">'+
    'Masculino'+
'</label>'+
'</div>'+'<div class="form-check mb-0">'+
    '<input class="form-check-input" type="radio"  name="inputradiosexo">'+
'<label class="form-check-label">'+
    'Femnino'+
'</label>'+
'</div>'+'</div>'         
        
//Z1.1 OBTENER INPUT - RADIO SELECCIONADO
Nombre = document.getElementsByName("inputradiosexo")         
        
function obtenerinputradiosexo() {//2.1 Listado con los Valores
    listadoNombre = [`'Masculino'`,`'Femnino'`]

    //3.1 Obtiene los input radio 
    var ele = document.getElementsByName("inputradiosexo");
    //3.1.1 Evalua uno por uno para encontrar con el seleccionado
    for(i = 0; i < ele.length; i++) {
        if(ele[i].checked){
        //3.1.2 Guarda su Valor
        //alert(listadoNombre[i])
        return listadoNombre[i]
        }
    }
    
}         
        
//----------------------------------------------------------------
//[R1.0 GRUPO RADIO - GRUPO INPUT ]
contenidoform += '<div class="col-md-12 mb-4">'+
'<div class="col-md-2 mb-0 input-group-sm">'+
    '<span class="input-group-text">pais</span>'+
'</div>'+'<div class="form-check mb-0">'+
    '<input class="form-check-input" type="radio"  name="inputradiopais">'+
'<label class="form-check-label">'+
    'Guatemala'+
'</label>'+
'</div>'+'<div class="form-check mb-0">'+
    '<input class="form-check-input" type="radio"  name="inputradiopais">'+
'<label class="form-check-label">'+
    'El Salvador'+
'</label>'+
'</div>'+'<div class="form-check mb-0">'+
    '<input class="form-check-input" type="radio"  name="inputradiopais">'+
'<label class="form-check-label">'+
    'Honduras'+
'</label>'+
'</div>'+'</div>'         
        
//Z1.1 OBTENER INPUT - RADIO SELECCIONADO
Nombre = document.getElementsByName("inputradiopais")         
        
function obtenerinputradiopais() {//2.1 Listado con los Valores
    listadoNombre = [`'Guatemala'`,`'El Salvador'`,`'Honduras'`]

    //3.1 Obtiene los input radio 
    var ele = document.getElementsByName("inputradiopais");
    //3.1.1 Evalua uno por uno para encontrar con el seleccionado
    for(i = 0; i < ele.length; i++) {
        if(ele[i].checked){
        //3.1.2 Guarda su Valor
        //alert(listadoNombre[i])
        return listadoNombre[i]
        }
    }
    
}         
        
//----------------------------------------------------------------
//[B 1.0 BOTON - BUTTON | INFO]
contenidoform += '<div class="row ">'+
    '<button type="button" class="btn btn-secondary btn-lg col-md-2 mb-4" onclick="infovalor()">Valor</button>'+
'</div>'         
            
    //3.1 Evento
    function infovalor(){
        //alert("info")
        console.log(`formulario ~>> [
    <
        tipo: "etiqueta",
        valor: "Nombre:"
    >,
    <
        tipo: "texto",
        valor: "Nombre",
        fondo: "Ingrese nombre"
    >,
    <
        tipo: "grupo-radio",
        nombre: "sexo",
        valores: ['Masculino', 'Femnino']
    >,
    <
        tipo: "grupo-radio",
        nombre: "pais",
        valores: ['Guatemala', 'El Salvador','Honduras']
    >,
    <
        tipo: "boton",
        valor: "Valor",
        evento: <EVENTO>
    >
]`)        
        //Crear iframe
        //Obtener div donde se colocara los elementos del formulario
        divcontenido = document.getElementById("contenidoformulario")
        divcontenido.innerHTML += `<br>
        <h3>Iframe Info</h3> 
        <iframe src="iframe_info.html" height="800" width="600" title="Iframe Info"></iframe>
        <br>`


    }         
            
             
        
divcontenido.innerHTML = contenidoform