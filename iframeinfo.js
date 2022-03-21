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
        nombre: "sexo",
        valores: ['Masculino', 'Femnino']
    >,
    <
        tipo: "grupo-radio",
        nombre: "pais",
        valores: ['Guatemala', 'El Salvador','Honduras']
    >,
    <
        tipo: "etiqueta",
        valor: "Tipo de color de ojos:"
    >,
    <
        tipo: "grupo-option",
        nombre: "Color ojos",
        valores: ['Cafe', 'Verde','Azules', 'No se que color son']
    >,
    <
        tipo: "boton",
        valor: "Info",
        evento: <info>
    >,
    <
        tipo: "boton",
        valor: "Entrada",
        evento: <entrada>
    >
]`;         
            
    console.log(texto);         
            
    divcontenido.innerHTML = "<p>"+ texto + "</h4>"; 