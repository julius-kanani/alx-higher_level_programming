#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(movieUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Status Code ${response.statusCode}`);
    return;
  }

  try {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  } catch (error) {
    console.error('Error parsing JSON:', error);
  }
});
