// Attendez que le document soit complètement chargé avant de manipuler le DOM
document.addEventListener('DOMContentLoaded', function() {
  // Sélectionner l'élément avec l'ID 'red_header'
  const redHeader = document.getElementById('red_header');

  // Sélectionner l'élément <header>
  const header = document.querySelector('header');

  // Ajouter un écouteur d'événement pour le clic
  redHeader.addEventListener('click', function() {
    // Ajouter la classe 'red' à l'élément <header>
    header.classList.add('red');
  });
});
