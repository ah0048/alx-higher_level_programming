#!/usr/bin/node
const request = require('request');
const UrlFilms = process.argv[2];
request.get(UrlFilms, (err, resp, body) => {
  if (err) {
    console.error(err);
  } else {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, film) => {
      return film.characters.find((character) => character.endsWith('/18/')) ? count + 1 : count;
    }, 0));
  }
});
