#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (err, res, body) => {
  const data = JSON.parse(body);
  const movies = data.results;

  let count = 0;
  movies.forEach(movie => {
    movie.characters.forEach(people => {
      if (people.includes('18')) {
        count++;
      }
    });
  });
  if (err) {
    console.error(err);
  }
  console.log(count);
});
