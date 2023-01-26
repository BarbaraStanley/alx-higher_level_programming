// script that fetches and lists the title for all movies by using given URL

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data){
for ( title = 0, title < len(data), title++ ) {
$('UL#list_movies').append(`<li>${data.title}</li>`);
}
});
