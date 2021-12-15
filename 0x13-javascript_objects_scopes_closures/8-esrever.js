#!/usr/bin/node
exports.esrever = function (list) {
  let i;
  const newList = [];
  for (i = list.length - 1; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
