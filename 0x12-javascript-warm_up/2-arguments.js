#!/usr/bin/node

const argl = process.argv.length;

if (argl === 2) {
  console.log('No argument');
} else if (argl === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
