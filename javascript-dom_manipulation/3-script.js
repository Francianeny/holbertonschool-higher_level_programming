// Attendez que le document soit complètement chargé avant de manipuler le DOM
document.addEventListener('DOMContentLoaded', function() {
  // Sélectionner l'élément avec l'ID 'toggle_header'
  const toggleHeader = document.getElementById('toggle_header');

  // Sélectionner l'élément <header>
  const header = document.querySelector('header');

  // Ajouter un écouteur d'événement pour le clic
  toggleHeader.addEventListener('click', function() {
    // Vérifier la classe actuelle de l'élément <header> et basculer la classe
    if (header.classList.contains('red')) {
      header.classList.remove('red');
      header.classList.add('green');
    } else if (header.classList.contains('green')) {
      header.classList.remove('green');
      header.classList.add('red');
    }
  });
});
