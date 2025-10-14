const { log } = require("console");
const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split("\n")
// console.log(input)

for (let A of input) {
    const x = A.split(" ");

    // console.log(x[0], x[1])
    let Start = Number(x[0])
    let End = Number(x[1])

    let cnt = 0;

    for (let i = Start; i<=End; i++) {
        
        // console.log("is here?")
        let str = i.toString();
        const set = new Set();
        
        let flag = true;

        for (const xx of str) {
            if (set.has(xx)) {
                flag = false;
                break;
            } else {
                set.add(xx)
            }
        }

        if (flag) cnt++;
    }

    console.log(cnt)

}

