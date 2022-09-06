#!/usr/bin/node

// Adds two numbers
exports.add = function (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return (NaN);
  } else {
    return (a + b);
  }
};
