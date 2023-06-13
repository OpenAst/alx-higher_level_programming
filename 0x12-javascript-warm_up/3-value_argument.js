#!/usr/bin/node

const { argv } = require('process);

let length = 0;

argv.forEach(() => length++);

console.log(length == 2 ? 'No argument' : argv[2]);
