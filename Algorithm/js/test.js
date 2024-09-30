let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const N = input[0];
let numbers = [];

for (let i = 1; i <= N; i++) {
  if (input[i] != "") {
    numbers.push(input[i].split(" "));
  }
}

for (let i = 0; i < numbers.length; i++) {
  let ans = 0;
  let n = Number(numbers[i][0]);
  let m = Number(numbers[i][1]);
  for (let b = 2; b < n; b++) {
    for (let a = 1; a < b; a++) {
      let tmp = (a ** 2 + b ** 2 + m) / (a * b);
      if (tmp === Math.floor(tmp)) {
        ans++;
      }
    }
  }
  console.log(ans);
}
