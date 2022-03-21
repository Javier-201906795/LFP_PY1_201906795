//0.0Obtener div donde se colocara los elementos del formulario
divcontenido = document.getElementById("contenidoformulario");
contenidoform = '';//----------------------------------------------------------------
//[L1.0 LABEL ]
contenidoform += '<label class="mb-3">Nombre:</label>'         
        
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
        return [inputE.value, `Nombre`]
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
        return [listadoNombre[i],`sexo`]
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
        return [listadoNombre[i],`pais`]
        }
    }
    
}         
        
//----------------------------------------------------------------
//[L1.0 LABEL ]
contenidoform += '<label class="mb-3">Tipo de color de ojos:</label>'         
        
//----------------------------------------------------------------
//[ S 1.0 GRUPO OPTION - SELECT ]
contenidoform += '<div class="input-group mb-3">'+
'<div class="input-group-prepend col-md-2">'+
    '<label class="input-group-text" >Color ojos</label>'+
'</div>'+
'<select class="custom-select col-md-3" id="selectcolorojos">'+
    '<option value="0" selected>Selecciona una opcion</option>';//9.1.1 Evalua uno por uno
    Lista1 = [`'Cafe'`,`'Verde'`,`'Azules'`,`'No se que color son'`]
    for(i = 0; i < Lista1.length; i++) {
        contenidoform += '<option value="'+Lista1[i]+'">'+Lista1[i]+'</option>';
    }         
        
contenidoform += '</select>'+
'</div>'
         
        
//3.1 Obtener opcion seleccionadas
function obtenerselectcolorojos(){
    selectNombre1 = document.getElementById("selectcolorojos")
    return [selectNombre1.value,`Color ojos`]
}         
        
//----------------------------------------------------------------
//[B 1.0 BOTON - BUTTON | INFO]
contenidoform += '<div class="row ">'+
    '<button type="button" class="btn btn-secondary btn-lg col-md-2 mb-4" onclick="infoinfo()">Info</button>'+
'</div>'         
            
    //3.1 Evento
    function infoinfo(){
        //alert("info")
        console.log(`N/A`)        
        //Crear iframe
        //Obtener div donde se colocara los elementos del formulario
        divcontenido = document.getElementById("contenidoformulario")
        divcontenido.innerHTML += `<br>
        <h3>Iframe Info</h3> 
        <iframe src="iframe_info.html" height="800" width="600" title="Iframe Info"></iframe>
        <br>`


    }         
            
             
        
//----------------------------------------------------------------
//[B 1.0 BOTON - BUTTON | ENTRADA]
contenidoform += '<div class="row ">'+
    '<button type="button" class="btn btn-primary btn-lg col-md-2 mb-4" onclick="entradaentrada()">Entrada</button>'+
'</div>'         
            
    //3.1 Evento
    function entradaentrada(){
                 
            
    var ListadoDatos = [];         
            
      console.log(obtenerinputtextnombre());         
            
     
            ListadoDatos.push(obtenerinputtextnombre());
              console.log(obtenerinputradiosexo());         
            
     
            ListadoDatos.push(obtenerinputradiosexo());
              console.log(obtenerinputradiopais());         
            
     
            ListadoDatos.push(obtenerinputradiopais());
              console.log(obtenerselectcolorojos());         
            
     
            ListadoDatos.push(obtenerselectcolorojos());
            console.log("-------");
            console.log(ListadoDatos[1]);
            console.log("-------");texto = "";
            for (i=0;i < ListadoDatos.length;i++){
                for (j=1;j >= 0;j--){
                    texto += ListadoDatos[i][j] + " | " 
                }
            }
            
            divcontenido = document.getElementById("contenidoformulario");
            divcontenido.innerHTML += texto;
        }         
            
             
        
divcontenido.innerHTML = contenidoform