#!/usr/bin/node
const n = parseInt(process.argv[2]);
if (!isNaN(n)) {
  console.log('My Number: ' + n);
} else {
  console.log('Not a number');
}
