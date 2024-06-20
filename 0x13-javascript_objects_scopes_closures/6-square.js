#!/usr/bin/node
const SquareParent = require('./5-square');
class Square extends SquareParent {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.width; i++) {
        console.log('C'.repeat(this.width));
      }
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
