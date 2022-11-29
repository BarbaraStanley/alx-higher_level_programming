#!/usr/bin/node
const y = require('./4-rectangle.js');
class Square extends y {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
