document.addEventListener('DOMContentLoaded', function() {
    var togglePassword = document.getElementById('toggle-password');
    var passwordField = document.getElementById('password');
    
    togglePassword.addEventListener('click', function() {
        var type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordField.setAttribute('type', type);
        this.querySelector('i').classList.toggle('fa-eye');
        this.querySelector('i').classList.toggle('fa-eye-slash');
    });
});
