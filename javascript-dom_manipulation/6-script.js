// Attendez que le document soit complètement chargé avant de manipuler le DOM
document.addEventListener('DOMContentLoaded', function() {
  // URL de l'API à partir de laquelle nous devons récupérer les données
  const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

  // Sélectionner l'élément avec l'ID 'character'
  const characterDiv = document.getElementById('character');

  // Utiliser la Fetch API pour récupérer les données
  fetch(apiUrl)
    .then(response => {
      // Vérifier si la réponse est ok (statut 200-299)
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      // Convertir la réponse en JSON
      return response.json();
    })
    .then(data => {
      // Accéder au nom du personnage et le mettre à jour dans l'élément HTML
      characterDiv.textContent = data.name;
    })
    .catch(error => {
      // En cas d'erreur, afficher un message dans la console
      console.error('There has been a problem with your fetch operation:', error);
    });
});
