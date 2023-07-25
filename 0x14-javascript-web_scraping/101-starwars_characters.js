#!/usr/bin/node

const request = require('request');

async function fetchCharacterData(characterUrl) {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      }
    });
  });
}

async function getMovieCharacters(movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  try {
    const movieResponse = await new Promise((resolve, reject) => {
      request.get(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body));
        }
      });
    });

    const characters = movieResponse.characters;
    for (const characterUrl of characters) {
      const characterName = await fetchCharacterData(characterUrl);
      console.log(characterName);
    }
  } catch (error) {
    console.log(error);
  }
}

const id = process.argv[2];

if (!id) {
  console.error('Usage: node scriptName.js <movie_id>');
} else {
  getMovieCharacters(id);
}

