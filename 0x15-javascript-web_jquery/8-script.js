$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const results = data.results;
  $.each(results, function (index, result) {
    $('UL#list_movies').append('<li>' + result.title + '</li>');
  });
});
