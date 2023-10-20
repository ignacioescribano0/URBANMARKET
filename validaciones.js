const formulario = document.getElementById('formulario');


const inputs = document.querySelectorAll('#formulario input');


const textarea = document.getElementById('textArea');


const asunto = document.getElementById('asunto');


const expresiones = {
    nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    dni: /^\d{7,9}$/, // 7 a 9 numeros.
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
    telefono: /^\d{9,14}$/, // 9 a 14 numeros.,
    texto: /^.{1,1000}$/,
    tarjeta: /^\d{10}$/, // 10 numeros.
}




const campos = {
    nombre: false,
    dni: false,
    correo: false,
    telefono: false,
    texto: false,
    asunto: false,
    tarjeta: true,
}




const validarFormulario = (e) => {
    switch (e.target.id) {
        case "nombre":
            validarCampo(expresiones.nombre, e.target, 'nombre');
            break;
        case "dni":
            validarCampo(expresiones.dni, e.target, 'dni');
            break;
        case "correo":
            validarCampo(expresiones.correo, e.target, 'correo');
            break;
        case "telefono":
            validarCampo(expresiones.telefono, e.target, 'telefono');
            break;
        case "textArea":
            validarCampo(expresiones.texto, e.target, 'texto');
            break;

        case "tarjeta":

            var chkSi = document.getElementById("chkSi");



            if (chkSi.checked == true) {
                const grupo = document.getElementById('grupo__nombretarjeta');
                if (expresiones.tarjeta.test(e.target.value)) {
                    grupo.classList.remove('formulario__grupo-incorrecto');
                    grupo.classList.add('formulario__grupo-correcto');
                    document.querySelector(`#grupo__nombretarjeta i`).classList.add('fa-check-circle');
                    document.querySelector(`#grupo__nombretarjeta i`).classList.remove('fa-circle-xmark');
                    document.querySelector(`#grupo__nombretarjeta p`).classList.remove('formulario__input-error-activo');
                    document.querySelector(`#grupo__nombretarjeta p`).classList.add('formulario__input-error');
                    campos['tarjeta'] = true;
                } 
                else {
                    grupo.classList.remove('formulario__grupo-correcto');
                    grupo.classList.add('formulario__grupo-incorrecto');
                    document.querySelector(`#grupo__nombretarjeta i`).classList.add('fa-circle-xmark');
                    document.querySelector(`#grupo__nombretarjeta i`).classList.remove('fa-check-circle');
                    document.querySelector(`#grupo__nombretarjeta p`).classList.add('formulario__input-error-activo');
                    document.querySelector(`#grupo__nombretarjeta p`).classList.remove('formulario__input-error');
                    campos['tarjeta'] = false;
                }
            }

            else {
                campos['tarjeta'] = true;
            }



            break;







        case "asunto":
            const grupo = document.getElementById('grupo__asunto');

            if (e.target.value !== "Seleccionar") {
                grupo.classList.remove('formulario__grupo-incorrecto');
                grupo.classList.add('formulario__grupo-correcto');
                document.querySelector(`#grupo__asunto p`).classList.remove('formulario__input-error-activo');
                document.querySelector(`#grupo__asunto p`).classList.add('formulario__input-error');
                campos['asunto'] = true;
            } else {
                grupo.classList.remove('formulario__grupo-correcto');
                grupo.classList.add('formulario__grupo-incorrecto');
                document.querySelector(`#grupo__asunto p`).classList.add('formulario__input-error-activo');
                document.querySelector(`#grupo__asunto p`).classList.remove('formulario__input-error');
                campos['asunto'] = false;
            }
            break;



    }
}


const validarCampo = (expresion, input, campo) => {
    const grupo = document.getElementById(`grupo__${campo}`);
    const valor = input.value.trim();


    if (expresion.test(input.value) || (campo === "texto" && valor !== "")) {
        grupo.classList.remove('formulario__grupo-incorrecto');
        grupo.classList.add('formulario__grupo-correcto');
        document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
        document.querySelector(`#grupo__${campo} i`).classList.remove('fa-circle-xmark');
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos[campo] = true;
    } else {
        grupo.classList.add('formulario__grupo-incorrecto');
        grupo.classList.remove('formulario__grupo-correcto');
        document.querySelector(`#grupo__${campo} i`).classList.add('fa-circle-xmark');
        document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
        campos[campo] = false;
    }
}










inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
});


textarea.addEventListener('keyup', validarFormulario);
textarea.addEventListener('blur', validarFormulario);


asunto.addEventListener('keyup', validarFormulario);
asunto.addEventListener('blur', validarFormulario);


asunto.addEventListener('change', validarFormulario);
asunto.addEventListener('keyup', validarFormulario);
asunto.addEventListener('blur', validarFormulario);


formulario.addEventListener('submit', (e) => {
    e.preventDefault();

    console.log("Formulario enviado");



    if (Object.values(campos).every(valor => valor === true)) {
        formulario.reset();
        for (const campo in campos) {
            if(campo !== "tarjeta") {
                campos[campo] = false;
            }else{
                campos[campo] = true; 
            }
        };
        document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
        document.getElementById('formulario__mensaje').classList.remove('formulario__mensaje-activo');
        setTimeout(() => {
            document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo');
        }, 5000);


        document.querySelectorAll('.formulario__grupo-correcto').forEach((icono) => {
            icono.classList.remove('formulario__grupo-correcto');
        });
    } else {
        document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
    }
});


function habilitaDesabilitaTarjeta() {
    var chkSi = document.getElementById("chkSi");
    var campoTarjeta = document.getElementById("tarjeta");
    if (chkSi.checked == true) {
        campoTarjeta.disabled = false;
        campos['tarjeta']=false;
    }
    else {
        campoTarjeta.value = ""
        campoTarjeta.disabled = true;
         campos['tarjeta']=true;
    }

}

