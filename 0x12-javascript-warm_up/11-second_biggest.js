#!/usr/bin/node

const myArray = process.argv.slice(2);
const arrayLength = myArray.length;

if (arrayLength < 2) {
  console.log('0');
} else {
  myArray.sort();
  console.log(myArray[myArray.length - 2]);
}
