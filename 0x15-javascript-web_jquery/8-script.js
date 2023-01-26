// script that fetches and lists the title for all movies by using given URL

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  $('UL#list_movies').append(data.results.map(movie => `<li>${data.title}</li>`));
});
