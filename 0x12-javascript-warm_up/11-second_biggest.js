#!/usr/bin/node
const args = process.argv.slice(2);
const array = [];
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  for (let i = 0; i < args.length; i++) {
    array[i] = parseInt(args[i], 10);
  }
  array.sort((a, b) => b - a);
  console.log(array[1]);
}
