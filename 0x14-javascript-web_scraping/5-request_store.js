#!/usr/bin/node
//  a script that gets the contents of a webpage and stores it in a file

const args = process.argv;
const fs = require('fs');
const request = require('request');
const url = args[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  fs.writeFileSync(args[3], body, 'utf-8');
});
