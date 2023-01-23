#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present

const args = process.argv;
const request = require('request');
const url = args[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  let count = 0;
  const result = JSON.parse(body).results;
  result.forEach(element => {
    (element.characters).forEach(news => {
      if (news.includes('18')) {
        count++;
      }
    });
  });
  console.log(count);
});
