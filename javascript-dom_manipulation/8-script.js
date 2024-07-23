// Utiliser l'événement DOMContentLoaded pour s'assurer que le DOM est complètement chargé
document.addEventListener('DOMContentLoaded', () => {
  // URL de l'API à partir de laquelle nous devons récupérer les données
  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Sélectionner l'élément avec l'ID 'hello'
  const helloDiv = document.getElementById('hello');

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
      // Accéder à la valeur du "hello" dans les données et mettre à jour l'élément HTML
      helloDiv.textContent = data.hello;
    })
    .catch(error => {
      // En cas d'erreur, afficher un message dans la console
      console.error('There has been a problem with your fetch operation:', error);
    });
});
