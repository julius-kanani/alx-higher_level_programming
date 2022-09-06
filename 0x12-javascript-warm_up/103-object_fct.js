#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

// A new function that increments the integer value.
myObject.incr = function () {
  return this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
