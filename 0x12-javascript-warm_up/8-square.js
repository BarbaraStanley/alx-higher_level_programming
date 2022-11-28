#!/usr/bin/node
const args = process.argv;
const conv = Number(args[2]);
if (isNaN(conv)) {
  console.log('Missing size');
} else {
  const i = 'X';
  for (let n = 0; n < conv; n++) {
    let e = '';
    for (let s = 0; s < conv; s++) {
      e += i;
    }
    console.log(e);
  }
}
