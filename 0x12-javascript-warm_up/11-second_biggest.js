#!/usr/bin/node
// second biggest integer in the list of arguments
const args = process.argv.slice(2).map((x) => {
  return parseInt(x);
});
if (args.length <= 1) {
  console.log(0);
} else {
  console.log(args.sort((a, b) => {
    return b - a;
  })[1]);
}
