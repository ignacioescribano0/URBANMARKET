  // Creo un objeto que contiene el elemento #contenido del DOM
  //  let HTML_a_mostrar = ""//document.querySelector('#contenido');
  
    
  hacerTrabajo()
  setInterval( hacerTrabajo, 3000); 
   
  function hacerTrabajo (){
        
    fetch('otros/clientes.txt') // Archivo a leer
            .then(response=>response.text())
            .then(TEXT=>parsea(TEXT))
        

    }
            
    
    function parsea(argumento) {
                    
                nameArr =argumento.split(',');

            fetch('https://randomuser.me/api/?results=2&nat=es')
            .then(datos => datos.json())
            .then(info=>muestraTarjeta(info))
                    
    }
    function muestraTarjeta(datos) {
                    // Actualiza el contenido del elemento HTML con el id "contenido".HTML_a_mostrar.innerHTML = nameArr[1];
                   
                    contenido.innerHTML = `
                    <h2  class="titulo_clientes" > LA OPINIÓN DE NUESTROS CLIENTES</h2> 
                        <div class="cliente1">
				            <div class="contenedorFotoYNombre">
                			    <div class="foto">
                            			<!-- Muestra una imagen obtenida de los datos de la API. -->
                            				<img src="${datos.results[0].picture.large}"</img>
                                </div>
                                <div>
                            			<!-- Muestra el nombre obtenido de los datos de la API. -->
                            			${datos.results[0].name.first}<br>   ${datos.results[0].name.last} 
					            </div>
				            </div>
                            <div class="feedback">
                                
                                <div><h3><q>${nameArr[Math.floor(Math.random() * 24)]}</q></h3></div>
				            </div>
                        </div>
                        <div class="cliente2">
				            <div class="contenedorFotoYNombre">
                			    <div class="foto">
                            			<!-- Muestra una imagen obtenida de los datos de la API. -->
                            				<img src="${datos.results[1].picture.large}"</img>
                                </div>
                                <div>
                            			<!-- Muestra el nombre obtenido de los datos de la API. -->
                            			${datos.results[1].name.first} <br> ${datos.results[1].name.last} 
					            </div>
				            </div>
                            <div class="feedback">
                                <div><h3><q>${nameArr[Math.floor(Math.random() * 24)]}</q></h3></div>
				            </div>
                        </div>
                        `;
                        
    }            
    