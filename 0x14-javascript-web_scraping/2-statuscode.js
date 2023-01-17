#!/usr/bin/node
// script that display the status code of a GET request

const args = process.argv
const request = require('request')
const url = args[2]

request(url, function (error, response, body) {
 if (error) {
  console.log(error);
 } else {
  console.log('code: {}' + JSON.parse(body));
 }
});
