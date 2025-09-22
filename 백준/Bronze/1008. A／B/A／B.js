const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim().split(" ");

const a = parseFloat(input[0]);
const b = parseFloat(input[1]);

console.log(a / b);
