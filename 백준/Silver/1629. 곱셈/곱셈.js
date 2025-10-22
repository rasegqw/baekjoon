const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split("\n");
const [A, B, C] = input[0].split(" ").map(BigInt)

let move = []
let target = B;

while (target != 1) {
    move.push(target);
    target = target/2n;
}

move = move.sort((a, b) => {return Number(a-b);});

let once = A%C;
let cur = once;

for (let i of move) {
    let res = (cur * cur) % C;

    if (i % 2n == 1) {
        res *= once;
        res %= C;
    }

    cur = res;
    // console.log(i, cur);    
}

console.log(Number(cur));