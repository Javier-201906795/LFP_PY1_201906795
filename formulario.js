//Obtener div donde se colocara los elementos del formulario
divcontenido = document.getElementById("contenidoformulario");//----------------------------------------------------------------
//[L1.0 LABEL ]
contenidoform = '<label class="mb-3">mario</label>'         
        
//----------------------------------------------------------------
//[T1.0 TEXTO - INPUT ]
contenidoform += '<div class="input-group input-group-sm mb-4">'+
'<div class="input-group-prepend col-md-2">'+
    '<span class="input-group-text">mario</span>'+
'</div>'+
'<div class="col-md-7">'+
    '<input type="text" class="form-control col-sm-2" aria-label="Small" placeholder="fondomario" id="inputtextmario">'+
'</div>'+
'</div>'         
        
//----------------------------------------------------------------
//[R1.0 GRUPO RADIO - GRUPO INPUT ]
contenidoform += '<div class="col-md-12 mb-4">'+
'<div class="col-md-2 mb-0 input-group-sm">'+
    '<span class="input-group-text">mario</span>'+
'</div>'+'<div class="form-check mb-0">'+
    '<input class="form-check-input" type="radio"  name="inputradiomario">'+
'<label class="form-check-label">'+
    'mario1'+
'</label>'+
'</div>'+'<div class="form-check mb-0">'+
    '<input class="form-check-input" type="radio"  name="inputradiomario">'+
'<label class="form-check-label">'+
    'mario2'+
'</label>'+
'</div>'+'</div>'         
        
//Z1.1 OBTENER INPUT - RADIO SELECCIONADO
Nombre = document.getElementsByName("inputradiomario")         
        
function obtenerinputradiomario() {//2.1 Listado con los Valores
    listadoNombre = ['mario1','mario2']

    //3.1 Obtiene los input radio 
    var ele = document.getElementsByName("inputradiomario");
    //3.1.1 Evalua uno por uno para encontrar con el seleccionado
    for(i = 0; i < ele.length; i++) {
        if(ele[i].checked)
        //3.1.2 Guarda su Valor
        alert(listadoNombre[i])
    }
    return listadoNombre[i]
}         
        
//----------------------------------------------------------------
//[R1.0 GRUPO RADIO - GRUPO INPUT ]
contenidoform += '<div class="col-md-12 mb-4">'+
'<div class="col-md-2 mb-0 input-group-sm">'+
    '<span class="input-group-text">mario</span>'+
'</div>'+'<div class="form-check mb-0">'+
    '<input class="form-check-input" type="radio"  name="inputradiomario">'+
'<label class="form-check-label">'+
    'mario1'+
'</label>'+
'</div>'+'<div class="form-check mb-0">'+
    '<input class="form-check-input" type="radio"  name="inputradiomario">'+
'<label class="form-check-label">'+
    'mario2'+
'</label>'+
'</div>'+'</div>'         
        
//Z1.1 OBTENER INPUT - RADIO SELECCIONADO
Nombre = document.getElementsByName("inputradiomario")         
        
function obtenerinputradiomario() {//2.1 Listado con los Valores
    listadoNombre = ['mario1','mario2']

    //3.1 Obtiene los input radio 
    var ele = document.getElementsByName("inputradiomario");
    //3.1.1 Evalua uno por uno para encontrar con el seleccionado
    for(i = 0; i < ele.length; i++) {
        if(ele[i].checked)
        //3.1.2 Guarda su Valor
        alert(listadoNombre[i])
    }
    return listadoNombre[i]
}         
        
//----------------------------------------------------------------
//[ S 1.0 GRUPO OPTION - SELECT ]
contenidoform += '<div class="input-group mb-3">'+
'<div class="input-group-prepend col-md-2">'+
    '<label class="input-group-text" >mario</label>'+
'</div>'+
'<select class="custom-select col-md-3" id="selectmario">'+
    '<option value="0" selected>Selecciona una opcion</option>'+'<option value="Valores1">mario1</option>'+'<option value="Valores1">mario2</option>'+'</select>'+
'</div>'
         
        
//3.1 Obtener opcion seleccionadas
function obtenerselectmario(){
    selectNombre1 = document.getElementById("selectmario")
    return selectNombre1.value
}         
        
//----------------------------------------------------------------
//[B 1.0 BOTON - BUTTON | ENTRADA]
contenidoform += '<div class="row ">'+
    '<button type="button" class="btn btn-primary btn-lg col-md-2 mb-4" onclick="entradabotonmario()">boton mario</button>'+
'</div>'         
            
    //3.1 Evento
    function entradabotonmario(){
        alert("entrada")
        

    }         
            
             
        
divcontenido.innerHTML = contenidoform