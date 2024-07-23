// Attendez que le document soit complètement chargé avant de manipuler le DOM
document.addEventListener('DOMContentLoaded', function() {
  // Sélectionner l'élément avec l'ID 'update_header'
  const updateHeader = document.getElementById('update_header');

  // Sélectionner l'élément <header>
  const header = document.querySelector('header');

  // Ajouter un écouteur d'événement pour le clic
  updateHeader.addEventListener('click', function() {
    // Mettre à jour le texte de l'élément <header>
    header.textContent = 'New Header!!!';
  });
});
