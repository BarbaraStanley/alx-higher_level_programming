#!/usr/bin/node
const args = process.argv;
const converted = Number(args[2]);
if (isNaN(converted)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + converted);
}
