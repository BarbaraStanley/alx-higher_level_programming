#!/usr/bin/node
// script that writes a string to a file

const args = process.argv
const fs = require('fs')
fs.writeFileSync(args[2], args[3], 'utf-8')
