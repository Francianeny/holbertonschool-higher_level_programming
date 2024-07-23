// Attendez que le document soit complètement chargé avant de manipuler le DOM
document.addEventListener('DOMContentLoaded', function() {
  // Sélectionner l'élément avec l'ID 'red_header'
  const redHeader = document.getElementById('red_header');

  // Sélectionner l'élément <header>
  const header = document.querySelector('header');

  // Ajouter un écouteur d'événement pour le clic
  redHeader.addEventListener('click', function() {
    // Modifier la couleur du texte de l'élément <header>
    header.style.color = '#FF0000';
  });
});
