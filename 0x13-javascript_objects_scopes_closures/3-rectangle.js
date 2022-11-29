#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let square = '';
      for (let a = 0; a < this.width; a++) {
        square = square + 'X';
      }
      console.log(square);
    }
  }
}

module.exports = Rectangle;
