#!/usr/bin/node
const https = require('https');

const req = https.request(process.argv[2], res => {
  process.stdout.write(`code: ${res.statusCode}\n`);
});

req.on('error', error => {
  process.stdout.write(`code: ${error.statusCode}\n`);
});

req.end();
