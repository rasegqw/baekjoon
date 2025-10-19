const fs = require("fs")

const input = fs.readFileSync(0, "utf8").trim().split("\n")

const num = Number(input[0])

if (num == 1) console.log(0)
else {
    let nums = [1];
    let cnt = 0;
    let totalSet = new Set();

    while (true) {
        let nextNums = new Set();

        for (let x of nums) {
            if (!totalSet.has(x*3) && x*3 <= num) {
                totalSet.add(x*3);
                nextNums.add(x*3);
            }
            if (!totalSet.has(x*2) && x*2 <= num) {
                totalSet.add(x*2);
                nextNums.add(x*2);
            }
            if (!totalSet.has(x+1)) {
                totalSet.add(x+1);
                nextNums.add(x+1);
            }
            
        }

        nums = Array.from(nextNums).sort((a, b) => b-a);
        // console.log(nums)
        
        if (nextNums.has(num)) {
            console.log(cnt+1);
            break;
        }

        cnt++;
    }
}