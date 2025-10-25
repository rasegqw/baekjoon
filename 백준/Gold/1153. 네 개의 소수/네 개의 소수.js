const fs = require("fs")

const input = fs.readFileSync(0, "utf8").trim().split("\n")

const [N] = input[0].split(" ").map(Number)

if (N < 8) console.log(-1);

let p = 0;

if (N % 2 == 0) p = 4;
else p = 5;

let sosuList = [2,3,5,7];

for (let i = 8; i<N-4; i++) {
    let x = Number.parseInt(Math.sqrt(i));
    // console.log(x);
    let isSosu = true;
    for (let j = 2; j<=x; j++) {
        if (i%j == 0) isSosu = false;
    }
    if (isSosu) sosuList.push(i);
}


for (let i of sosuList) {
    for (let j of sosuList) {
        if (i+j == N-p) {
            if (p == 4) console.log("2 2 "+i+" "+j);
            else console.log("2 3 "+i+" "+j);
            return;
        }
    }
}

console.log(-1)