#!/usr/bin/node

const firstArgument = process.argv[2];
if (isNaN(firstArgument)) {
  console.log('Not a Number');
} else {
  console.log('My Number: ' + firstArgument);
}
