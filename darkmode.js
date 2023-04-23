function toggleDarkMode() {
    var body = document.body;
    var button = document.getElementById('dark-mode-btn');
    
    if (body.classList.contains('dark-mode')) {
        body.classList.remove('dark-mode');
        button.innerHTML = "Dark Mode";
    } else {
        body.classList.add('dark-mode');
        button.innerHTML = "Light Mode";
    }
}
