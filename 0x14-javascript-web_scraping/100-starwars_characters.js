#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie details:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error Status Code:', response.statusCode);
    return;
  }

  try {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    characters.forEach(characterUrl => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error fetching character details:', error);
          return;
        }

        if (response.statusCode !== 200) {
          console.error('Unexpected character status code:', error);
          return;
        }

        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    });
  } catch (error) {
    console.error('Error parsing movieData JSON:', error);
  }
});
