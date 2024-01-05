#!/usr/bin/node

const firstArgv = process.argv[2];
const x = parseInt(firstArgv, 10);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let count = 1;
  while (count <= x) {
    console.log('C is fun');
    count++;
  }
}
