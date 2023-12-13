#!/usr/bin/node

let track = 0;

exports.logMe = function (item) {
  console.log(`${track}: ${item}`);
  track++;
};
