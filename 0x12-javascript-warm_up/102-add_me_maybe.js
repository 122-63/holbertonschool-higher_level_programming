#!/usr/bin/node
// Write a function that increments and calls a function
exports.addMeMaybe = (n, f) => {
  return f(n + 1);
};
