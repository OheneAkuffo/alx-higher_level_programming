#!/usr/bin/node
/*
 * a class Rectangle that defines a rectangle
 * onstructor must take 2 arguments: w and h
 * Initialize the instance attribute width with the value of w
 * Initialize the instance attribute height with the value of h
 * If w or h is equal to 0 or not a positive integer, create an empty object
 * an instance method called print() that prints the rectangle using the character
 */

class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let count = 1;
    while (count <= this.height) {
      for (let x = 1; x <= this.width; x++) {
        process.stdout.write('X');
      }
      count++;
      console.log();
    }
  }
}

module.exports = Rectangle;
