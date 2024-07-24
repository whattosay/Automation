// theme-toggle.js

document.addEventListener('DOMContentLoaded', function () {
    const themeToggleButton = document.getElementById('theme-toggle');
    const icon = themeToggleButton.querySelector('i');

    themeToggleButton.addEventListener('click', function () {
        document.body.classList.toggle('dark-theme');
        if (document.body.classList.contains('dark-theme')) {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
        } else {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
        }
    });

    // Initialize the icon based on the current theme
    if (document.body.classList.contains('dark-theme')) {
        icon.classList.add('fa-moon');
    } else {
        icon.classList.add('fa-sun');
    }
});