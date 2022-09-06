#!/usr/bin/node

const firstArgument = process.argv[2];

// Compute factorial of a given number.
function factorial (number) {
  if (number < 2 || isNaN(number)) {
    return (1);
  } else {
    return (number * factorial(number - 1));
  }
}

console.log(factorial(parseInt(firstArgument)));
