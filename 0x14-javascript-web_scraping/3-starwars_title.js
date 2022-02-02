#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, (err, res, body) => {
  const movie = JSON.parse(body);
  console.log(movie.title);

  if (err) {
    console.error(err);
  }
});
