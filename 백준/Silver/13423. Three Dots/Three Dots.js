const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split("\n")

const T = Number(input[0])

for (let i = 0; i<T; i++) {
    const N = Number(input[i*2+1]);

    let dots = input[i*2+2].split(" ").map(Number);

    dots.sort((a, b) => a-b);

    // console.log(dots)

    let setMidVal = new Set();
    let cnt = 0;

    for (let j = 1; j<N-1; j++) setMidVal.add(dots[j]*2);

    for (let left = 0; left<N-2; left++) {
        for (let right = left+2; right<N; right++) {
            if (setMidVal.has(dots[left]+dots[right])) cnt++;
        }
    }

    console.log(cnt)
}