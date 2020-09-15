#!/usr/bin/node
const Integer = parseInt(process.argv[2]);
if (!isNaN(Integer)) {
  console.log('My Number: ' + Integer);
} else {
  console.log('Not a number');
}
