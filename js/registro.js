document.getElementById('form').addEventListener ('submit', function(event) {
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const password2 = document.getElementById('password2').value;

    const usernameError = document.querySelector('#username + .error');
    const emailError = document.querySelector('#email + .error');
    const passwordError = document.querySelector('#password + .error');
    const password2Error = document.querySelector('#password2 + .error');

    usernameError.textContent = '';
    emailError.textContent = '';
    passwordError.textContent = '';
    password2Error.textContent = '';

    if (username.trim() === '') {
        usernameError.textContent = 'El nombre de usuario es requerido';
        event.preventDefault();
    }

  
    if (email.trim() === '') {
        emailError.textContent = 'El email es requerido';
        event.preventDefault();
    } else if (!validarEmail(email.trim())) {
        emailError.textContent = 'El email no es válido';
        event.preventDefault();
    }

   
    if (password.trim() === '') {
        passwordError.textContent = 'La contraseña es requerida';
        event.preventDefault();
    }

   
    if (password2.trim() !== password.trim()) {
        password2Error.textContent = 'Las contraseñas no coinciden';
        event.preventDefault();
    }
     
     if (usernameError.textContent === '' && emailError.textContent === '' && passwordError.textContent === '' && password2Error.textContent === '') {
        document.getElementById('usernameDisplay').textContent = username; 
        window.location.href = "index.html"; 

    }
});

function validarEmail(email) {
    const partes = email.split('@');
    if (partes.length !== 2 || partes[0].trim().length === 0 || partes[1].trim().length === 0) {
        return false;
    }

    const dominio = partes[1].split('.');
    if (dominio.length < 2 || dominio[dominio.length - 1].trim().length === 0) {
        return false;
    }

    return true;
}