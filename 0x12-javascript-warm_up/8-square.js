#!/usr/bin/node
// Write a script that prints a square
const size = parseInt(process.argv[2]);
const str = 'X';
if (Number.isInteger(size)) {
  for (let i = 0; i < size; i++) {
    console.log(str.repeat(size));
  }
} else {
  console.log('Missing size');
}
