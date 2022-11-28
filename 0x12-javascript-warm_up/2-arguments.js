#!/usr/bin/node

// import { argv } from 'node:process';
const args = process.argv;

args.forEach((val, index) => {
  if (index < 2) {
    console.log('No Argument');
  } else if (index === 2) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
});
