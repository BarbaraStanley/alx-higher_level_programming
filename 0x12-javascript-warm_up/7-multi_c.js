#!/usr/bin/node
const args = process.argv;
const conv = Number(args[2]);
if (isNaN(conv)) {
  console.log('Missing number of occurrences');
} else {
  const i = 'C is fun';
  for (let n = 0; n < conv; n++) {
    console.log(i);
  }
}
