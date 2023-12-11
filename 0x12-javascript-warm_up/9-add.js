#!/usr/bin/node

const firstArgv = process.argv[2];
const secondArgv = process.argv[3];

function add (a, b) {
  return a + b;
}

const x = parseInt(firstArgv, 10);
const y = parseInt(secondArgv, 10);

if (isNaN(x) || isNaN(y)) {
  console.log(NaN);
} else {
  console.log(add(x, y));
}
