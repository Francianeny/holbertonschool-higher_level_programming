// Attendez que le document soit complètement chargé avant de manipuler le DOM
document.addEventListener('DOMContentLoaded', function() {
  // URL de l'API à partir de laquelle nous devons récupérer les données
  const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

  // Sélectionner l'élément <ul> avec l'ID 'list_movies'
  const listMovies = document.getElementById('list_movies');

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
      // Accéder à la liste des films et pour chaque film créer un élément <li> avec le titre
      data.results.forEach(film => {
        const listItem = document.createElement('li');
        listItem.textContent = film.title;
        listMovies.appendChild(listItem);
      });
    })
    .catch(error => {
      // En cas d'erreur, afficher un message dans la console
      console.error('There has been a problem with your fetch operation:', error);
    });
});
