#!/usr/bin/node
/*
 * A class Rectangle that defines a rectangle
 * The constructor takes 2 arg, w and h
 */

class Rectangle {
  constructor (w = 0, h = 0) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
