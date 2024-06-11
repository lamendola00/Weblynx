document.addEventListener('DOMContentLoaded', function() {
    var togglePassword = document.getElementById('toggle-password');
    var passwordField = document.getElementById('password');
    var toggleConfirmPassword = document.getElementById('toggle-confirm-password');
    var confirmPasswordField = document.getElementById('confirm-password');
    
    togglePassword.addEventListener('click', function() {
        var type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordField.setAttribute('type', type);
        this.querySelector('i').classList.toggle('fa-eye');
        this.querySelector('i').classList.toggle('fa-eye-slash');
    });

    toggleConfirmPassword.addEventListener('click', function() {
        var type = confirmPasswordField.getAttribute('type') === 'password' ? 'text' : 'password';
        confirmPasswordField.setAttribute('type', type);
        this.querySelector('i').classList.toggle('fa-eye');
        this.querySelector('i').classList.toggle('fa-eye-slash');
    });
});
