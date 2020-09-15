#!/usr/bin/node
let Integer = parseInt(process.argv[2], 10);
if (Number.isInteger(Integer) && Integer > 0) {
  for (Integer; Integer !== 0; Integer--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
