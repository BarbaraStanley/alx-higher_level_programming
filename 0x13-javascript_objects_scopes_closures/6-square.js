#!/usr/bin/node
const y = require('./5-square.js');
class Square extends y {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let square = '';
      for (let a = 0; a < this.width; a++) {
        if (typeof (c) === 'undefined') {
          square = square + 'X';
        } else {
          square = square + c;
        }
      }
      console.log(square);
    }
  }
}

module.exports = Square;
