let input = require("fs").readFileSync("/dev/stdin").toString().split("\n");

const num = parseInt(input[0]);

const numArray = input.slice(1, num + 1).sort((a, b) => a - b);

console.log(numArray.join("\n"));
