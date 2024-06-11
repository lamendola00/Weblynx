document.addEventListener('DOMContentLoaded', function() {
    // Event listener per il menu a tendina
    var userDropdown = document.getElementById('userDropdown');
    userDropdown.addEventListener('click', function(event) {
        event.preventDefault();
        this.nextElementSibling.classList.toggle('show');
    });
    
    // Nasconde il menu a tendina quando si fa clic al di fuori
    window.addEventListener('click', function(event) {
        if (!event.target.matches('#userDropdown')) {
            var dropdowns = document.getElementsByClassName('dropdown-menu');
            for (var i = 0; i < dropdowns.length; i++) {
                var openDropdown = dropdowns[i];
                if (openDropdown.classList.contains('show')) {
                    openDropdown.classList.remove('show');
                }
            }
        }
    });
});
