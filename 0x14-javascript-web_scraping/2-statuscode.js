#!/usr/bin/node
const https = require('https');

const req = https.request(process.argv[2], res => {
  console.log(`code: ${res.statusCode}`);
});

req.on('error', error => {
  console.error(`code: ${error.statusCode}`);
});

req.end();
