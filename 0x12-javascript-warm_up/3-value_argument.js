#!/usr/bin/node

const args = process.argv;

args.forEach((value, index) => {
  if (index < 2) {
    console.log('No argument');
  } else {
    console.log(`${value}`);
  }
});
