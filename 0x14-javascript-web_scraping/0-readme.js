#!/usr/bin/node
// script that reads and prints the content of a file

const args = process.argv;
const filesys = require('fs');
const str = filesys.readFileSync(args[2], 'utf-8');
console.log(str);
