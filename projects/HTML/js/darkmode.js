function toggleDarkMode() {
    var body = document.body;
    var button = document.getElementById('dark-mode-btn');
    var title = document.querySelector('.titolo');
  
    if (body.classList.contains('dark-mode')) {
      body.classList.remove('dark-mode');
      button.innerHTML = "Dark Mode";
      title.style.color = "black"; // Cambia il colore del titolo in nero
    } else {
      body.classList.add('dark-mode');
      button.innerHTML = "Light Mode";
      title.style.color = "#0077cc"; // Cambia il colore del titolo in bianco
    }
  }
  