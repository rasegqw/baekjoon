const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split("\n")

// console.log(input)

const [N, M] = input[0].split(" ").map(Number)

// console.log(N, M)

const cakes = input[1].split(" ")

cakes.sort((a, b) => {
    const A = Number(a);
    const B = Number(b);
    const aDiv10 = A%10===0;
    const bDiv10 = B%10===0;
    
    if (!aDiv10 && bDiv10) return 1;
    else if (aDiv10 && !bDiv10) return -1;
    
    return A-B;
})

// console.log(cakes)

let cutCnt = 0;
let cakeCnt = 0;

for (let x of cakes) {
    const X = Number(x);
    if (X === 10) {
        cakeCnt++;
    } else if (X<10) {
        continue;
    } else {
        if (X%10 === 0) {
            cutCnt += parseInt(X/10 - 1);
            cakeCnt += parseInt(X/10);

            if (cutCnt > M) {
                cakeCnt -= (cutCnt-M) + 1;
                break;
            }
        } else {
            cutCnt += parseInt(X/10);
            cakeCnt += parseInt(X/10);

            if (cutCnt > M) {
                cakeCnt -= (cutCnt-M);
                break;
            }
        }
    }

    // console.log(cakeCnt, cutCnt)
}

console.log(cakeCnt);