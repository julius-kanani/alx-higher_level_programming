$(document).ready(function() {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function(response) {
      response.results.forEach(function(movie) {
        $('<li>').text(movie.title).appendTo('#list_movies');
      });
    }
  });
});
