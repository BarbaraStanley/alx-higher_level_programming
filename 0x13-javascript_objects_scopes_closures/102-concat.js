#!/usr/bin/node
const args = process.argv;
const fs = require('fs');

const str = fs.readFileSync(args[2], 'utf-8');
const str2 = fs.readFileSync(args[3], 'utf-8');

const file = str + str2;
fs.writeFileSync(args[4], file, 'utf-8');
