// Constructing the data object for AJAX request
var data_to_send = {
    csrf_token: $('#csrf_token').val(), // Add the CSRF token to the AJAX data
};


document.addEventListener('DOMContentLoaded', function() {
    function togglePasswordVisibility(toggleButtonId, passwordFieldId) {
        var toggleButton = document.getElementById(toggleButtonId);
        var passwordField = document.getElementById(passwordFieldId);

        toggleButton.addEventListener('click', function() {
            var type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordField.setAttribute('type', type);
            this.querySelector('i').classList.toggle('fa-eye');
            this.querySelector('i').classList.toggle('fa-eye-slash');
        });
    }

    // Gestione visibilità per le password
    togglePasswordVisibility('toggle-current-password', 'current-password');
    togglePasswordVisibility('toggle-new-password', 'new-password');
});
