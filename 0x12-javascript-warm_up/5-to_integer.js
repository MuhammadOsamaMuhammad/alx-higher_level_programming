#!/usr/bin/node
const convertedNum = Math.floor(+process.argv[2]);
console.log(isNaN(convertedNum) ? "Not a number" : `My number: ${convertedNum}`);
