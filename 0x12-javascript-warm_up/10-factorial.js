#!/usr/bin/node
// Write a script that computes and prints a factorial
function Factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * Factorial(n - 1);
  }
}
const nfact = parseInt(process.argv[2]);
console.log(Factorial(nfact));
