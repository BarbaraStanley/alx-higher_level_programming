#!/usr/bin/node
// a script that prints all characters of a Star Wars movie

const args = process.argv;
const request = require('request');
const id = args[2];
const url1 = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url1, function (error, response, body) {
  if (error) { console.error(error); }
  const character = JSON.parse(body).characters;
  character.forEach(name => getChar(name));
}
);
function getChar (url2) {
  request(url2, function (error, response, body) {
    if (error) { console.error(error); }
    console.log(JSON.parse(body).name);
  });
}
