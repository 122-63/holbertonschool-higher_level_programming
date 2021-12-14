#!/usr/bin/node
// function that executes x times a function
exports.callMeMoby = function (x, fun) {
  for (let i = 0; i < x; i++) fun();
};
