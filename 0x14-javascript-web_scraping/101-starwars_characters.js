#!/usr/bin/env node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./101-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(movieUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie details:', error);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  const fetchCharacter = (url, callback) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error('Error fetching character details:', error);
        callback(null);
      } else {
        const characterData = JSON.parse(body);
        callback(characterData.name);
      }
    });
  };

  const printCharacters = (url) => {
    if (url.length === 0) return;

    const characterUrl = url.shift();
    fetchCharacter(characterUrl, (name) => {
      if (name) {
        console.log(name);
      }
      printCharacters(url);
    });
  };

  printCharacters(characterUrls.slice());
});
