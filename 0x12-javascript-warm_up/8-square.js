#!/usr/bin/node
const Integer = parseInt(process.argv[2], 10);
let i = Integer;
if (Number.isInteger(Integer) && Integer > 0) {
  for (i; i !== 0; i--) {
      console.log('X'.repeat(Integer));
  }
} else if (!Number.isInteger(Integer)) {
  console.log('Missing size');
}
