#!/usr/bin/node
const args = process.argv;
const fs = require('fs');

let str = fs.readFileSync(args[2], 'utf-8');
let str2 = fs.readFileSync(args[3], 'utf-8');

let file = str+str2;
fs.writeFileSync(args[4], file, 'utf-8');
