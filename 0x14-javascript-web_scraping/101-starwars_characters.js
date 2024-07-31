#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(url, (err, resp, body) => {
  if (err) {
    console.error(err);
  } else {
    const characters = JSON.parse(body).characters;
    PrintAllCharacters(characters, 0);
  }
});

function PrintAllCharacters (characters, index) {
  request.get(characters[index], (err, resp, body) => {
    if (err) {
      console.error(err);
    }
    const CharacterInfo = JSON.parse(body);
    console.log(CharacterInfo.name);
    if (index + 1 < characters.length) {
      PrintAllCharacters(characters, index + 1);
    }
  });
}
