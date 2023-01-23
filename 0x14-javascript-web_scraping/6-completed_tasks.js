#!/usr/bin/node
// a script that computes the number of tasks completed by user id

const args = process.argv;
const request = require('request');
const url = args[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const test = JSON.parse(body);
  const dict = {};
  test.forEach(data => {
    if (data.completed === true) {
      if (data.userId in dict) {
        dict[data.userId] = dict[data.userId] + 1;
      } else {
        dict[data.userId] = 1;
      }
    }
  });
  console.log(dict);
});
