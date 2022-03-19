//Obtener div donde se colocara los elementos del formulario
divcontenido = document.getElementById("contenidoformulario");

//----------------------------------------------------------------
//[L1.0 LABEL ]
contenidoform = '<label> VALOR </label>'
contenidoform += '<br><br>'

//----------------------------------------------------------------
//[T1.0 TEXTO - INPUT ]
contenidoform += '<div class="input-group input-group-sm mb-4">'+
'<div class="input-group-prepend col-md-2">'+
'<span class="input-group-text">VALOR</span>'+
'</div>'+
'<div class="col-md-7">'+
    '<input type="text" class="form-control col-sm-2" aria-label="Small" placeholder="FONDO" >'+
'</div>'+
'</div>'


//----------------------------------------------------------------
//[R1.0 GRUPO RADIO - GRUPO INPUT ]
contenidoform += '<div class="col-md-2">'+
'<span class="input-group-text">NOMBRE</span>'+
'</div>'+
'<br>'+
'<div class="form-check">'+
'<input class="form-check-input" type="radio"  name="NOMBRE">'+
'<label class="form-check-label">'+
'Default radio'+
'</label>'+
'</div>'+
'<div class="form-check">'+
'<input class="form-check-input" type="radio"  name="NOMBRE">'+
'<label class="form-check-label">'+
'Default checked radio'+
'</label>'+
'</div>'

//1.1 OBTENER INPUT - RADIO SELECCIONADO
Nombre = document.getElementsByName('NOMBRE')

function obtenerNombre() {
    //2.1 Listado con los Valores
    listadoNombre = ["valor1","valor2","valor3"]

    //3.1 Obtiene los input radio 
    var ele = document.getElementsByName('NOMBRE');
    //3.1.1 Evalua uno por uno para encontrar con el seleccionado
    for(i = 0; i < ele.length; i++) {
        if(ele[i].checked)
        //3.1.2 Guarda su Valor
        
        document.getElementById("result").innerHTML
                = "NOMBRE: "+ele[i].value + i + listadoNombre[i];
    }
}


divcontenido.innerHTML = contenidoform