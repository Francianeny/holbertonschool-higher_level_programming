// Attendez que le document soit complètement chargé avant de manipuler le DOM
document.addEventListener('DOMContentLoaded', function() {
  // Sélectionner l'élément avec l'ID 'add_item'
  const addItem = document.getElementById('add_item');

  // Sélectionner l'élément <ul> avec la classe 'my_list'
  const list = document.querySelector('.my_list');

  // Ajouter un écouteur d'événement pour le clic
  addItem.addEventListener('click', function() {
    // Créer un nouvel élément <li>
    const newItem = document.createElement('li');
    // Définir le texte du nouvel élément <li>
    newItem.textContent = 'Item';
    // Ajouter le nouvel élément <li> à la liste
    list.appendChild(newItem);
  });
});
