#!/usr/bin/node
function factorial (num) {
  if (num === 1 || num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}
const args = process.argv.slice(2);
const num = parseInt([args[0]], 10);
if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}
