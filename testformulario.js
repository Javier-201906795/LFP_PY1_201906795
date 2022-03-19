//Obtener div donde se colocara los elementos del formulario
divcontenido = document.getElementById("contenidoformulario");

//[ LABEL ]
contenidoform = '<label> VALOR </label>'
contenidoform += '<br><br>'

//[ TEXTO - INPUT ]
contenidoform += '<div class="input-group input-group-sm mb-4">'+
'<div class="input-group-prepend col-md-2">'+
'<span class="input-group-text">VALOR</span>'+
'</div>'+
'<div class="col-md-7">'+
    '<input type="text" class="form-control col-sm-2" aria-label="Small" placeholder="FONDO" >'+
'</div>'+
'</div>'

//[ GRUPO RADIO - GRUPO INPUT ]

//OBTENER INPUT - RADIO SELECCIONADO
Nombre = document.getElementsByName('NOMBRE')

function obtenerNombre() {
    //Obtiene los input radio 
    var ele = document.getElementsByName('NOMBRE');
    //Evalua uno por uno para encontrar con el seleccionado
    for(i = 0; i < ele.length; i++) {
        if(ele[i].checked)
        document.getElementById("result").innerHTML
                = "NOMBRE: "+ele[i].value + i;
    }
}


divcontenido.innerHTML = contenidoform