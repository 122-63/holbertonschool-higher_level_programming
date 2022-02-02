#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url).on('response', response => {
  response.setEncoding('UTF8');
  response.on('data', data => {
    const movie = JSON.parse(data);
    console.log(movie.title);
  });
});
