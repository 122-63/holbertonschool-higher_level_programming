#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
  }
  const todos = JSON.parse(body);
  const users = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (!users[todo.userId]) {
        users[todo.userId] = 1;
      } else {
        users[todo.userId]++;
      }
    }
  });
  console.log(users);
});
