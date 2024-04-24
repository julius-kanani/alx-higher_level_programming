#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;
const character = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Status Code ${response.statusCode}`);
    return;
  }

  try {
    const filmsData = JSON.parse(body);
    let count = 0;

    for (const film of filmsData.results) {
      if (film.characters.includes(character)) {
        count++;
      }
    }

    console.log(count);
  } catch (error) {
    console.error('Error parsing JSON:', error);
  }
});
