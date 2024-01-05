#!/usr/bin/node

const firstArgv = process.argv[2];
const size = parseInt(firstArgv, 10);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  let count = 1;
  while (count <= size) {
    for (let i = 1; i <= size; i++) {
      process.stdout.write('X');
    }
    console.log();
    count++;
  }
}
