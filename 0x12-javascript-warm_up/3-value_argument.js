#!/usr/bin/node

const argc0 = process.argv[2];

if (argc0 !== undefined) {
  console.log(argc0);
} else {
  console.log('No argument');
}
