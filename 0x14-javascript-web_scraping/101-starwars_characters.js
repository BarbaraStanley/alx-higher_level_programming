#!/usr/bin/node
// script that prints all characters of a Star Wars movie in same order of list

const args = process.argv;
const request = require('request');
const id = args[2];
const url1 = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url1, function (error, response, body) {
  if (error) { console.error(error); }
  const character = JSON.parse(body).characters;
  getChar(character, 0);
});

function getChar (url2, order) {
  request(url2[order], function (error, response, body) {
    if (error) { console.error(error); }
    console.log(JSON.parse(body).name);
    if (order + 1 < url2.length) { getChar(url2, order + 1); }
  });
}
