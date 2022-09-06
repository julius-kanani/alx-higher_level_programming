#!/usr/bin/node

const firsNum = process.argv[2];
const secondNum = process.argv[3];

// Add two integers
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  } else {
    return parseInt(a) + parseInt(b);
  }
}

console.log(add(firsNum, secondNum));
