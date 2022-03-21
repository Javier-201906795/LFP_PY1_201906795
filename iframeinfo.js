//Obtener div donde se colocara los elementos 
divcontenido = document.getElementById("contenido");texto = `formulario ~>> [
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
        nombre: "pais",
        valores: ['Guatemala', 'El Salvador','Honduras']
    >,
    <
        tipo: "boton",
        valor: "Valor",
        evento: <EVENTO>
    >
]`;         
            
    console.log(texto);         
            
    divcontenido.innerHTML = "<p>"+ texto + "</h4>"; 