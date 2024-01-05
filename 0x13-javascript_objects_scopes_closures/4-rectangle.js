#!/usr/bin/node
/*
 * a class Rectangle that defines a rectangle
 * onstructor must take 2 arguments: w and h
 * Initialize the instance attribute width with the value of w
 * Initialize the instance attribute height with the value of h
 * If w or h is equal to 0 or not a positive integer, create an empty object
 * an instance method called print() that prints the rectangle using the character
 * an instance method called rotate() that exchanges the width and the height of the rectangle
 * an instance method called double() that multiples the width and the height of the rectangle by 2

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

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
