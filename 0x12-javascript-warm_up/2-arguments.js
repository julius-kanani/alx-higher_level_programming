#!/usr/bin/node

const arrayLength = process.argv.length;
if (arrayLength > 3) {
  console.log('Arguments found');
} else if (arrayLength === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
