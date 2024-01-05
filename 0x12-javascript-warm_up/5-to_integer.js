#!/usr/bin/node

const first = process.argv[2];

const numberValue = parseInt(first, 10);

if (!isNaN(numberValue)) {
  console.log('My number: ' + numberValue);
} else {
  console.log('Not a number');
}
