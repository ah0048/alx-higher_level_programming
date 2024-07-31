#!/usr/bin/node
const request = require('request');
const UrlFilms = process.argv[2];
const CharacterWanted = 'https://swapi-api.alx-tools.com/api/people/18/';
request.get(UrlFilms, (err, resp, body) => {
  let NumFilms = 0;
  if (err) {
    console.error(err);
  } else {
    body = JSON.parse(body);
    for (const result of body.results) {
      for (const character of result.characters) {
        if (CharacterWanted === character) {
          NumFilms += 1;
        }
      }
    }
    console.log(NumFilms);
  }
});
