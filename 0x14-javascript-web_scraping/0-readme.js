#!/usr/bin/node

/* File System Object */
const fs = require('fs');

/* Read File */
fs.readFile('3-starwars_title.js', bar);

function bar(err, data) {
  err
    ? Function('error', 'throw error')(err)
    : console.log(JSON.stringify(data));
}
