const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split("\n");
const [N, M] = input[0].split(" ").map(Number);

let trains = Array.from({ length:N }, () => Array(20).fill(false))

for (let j = 1; j<=M; j++) {
    const target = input[j].split(" ").map(Number);
    const trainNum = target[1]-1;

    // console.log(target, trainNum)

    switch (target[0]) {
        case 1:
            trains[trainNum][target[2]-1] = true;
            break;
        case 2:
            trains[trainNum][target[2]-1] = false;
            break;
        case 3:
            for (let cur = 19; cur>0; cur--) {
                trains[trainNum][cur] = trains[trainNum][cur-1];
            }
            trains[trainNum][0] = false;
            break;
        default:
            for (let cur = 0; cur<19; cur++) {
                trains[trainNum][cur] = trains[trainNum][cur+1];
            }
            trains[trainNum][19] = false;
            break;
    }
}

let pattern = new Set();
    
for (let train = 0; train<N; train++) {
    let res = 0;
    for (let n = 0; n<20; n++) {
        if (trains[train][n] == true) res += 1<<n;
    }
    // console.log(res);
    pattern.add(res);
}

console.log(pattern.size);