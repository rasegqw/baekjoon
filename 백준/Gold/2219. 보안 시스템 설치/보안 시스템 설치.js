const fs = require("fs")

const input = fs.readFileSync(0, "utf8").trim().split("\n")
const INF = 100_000_000
const [N, M] = input[0].split(" ").map(Number)

let relations = Array.from({length:N+1}, () => Array(N+1).fill(INF))
for (let i = 1; i<=N; i++) relations[i][i] = 0;

for (let i = 1; i<=M; i++) {
    const [A, B, C] = input[i].split(" ").map(Number)

    if (relations[A][B] > C) relations[A][B] = C;
    if (relations[B][A] > C)relations[B][A] = C;
}

for (let j = 1; j<=N; j++) {
    for (let i = 1; i<=N; i++) {
        for (let k = 1; k<=N; k++) {
            if (relations[i][j]+relations[j][k] < relations[i][k]) {
                relations[i][k] = relations[i][j]+relations[j][k];
            }
        }
    }
}

let minSum = Infinity;
let minSet = new Set();

for (let i = 1; i<=N; i++) {
    let sum = 0;
    for (let j = 1; j<=N; j++) {
        if (relations[i][j] != INF) {
            sum += relations[i][j];
        }
    }

    if (minSum > sum) {
        minSum = sum;
        minSet = new Set();
        minSet.add(i);
    } if (minSum == sum) {
        minSet.add(i);
    }
}

let minNum = Infinity

for (let i of minSet) {
    if (i < minNum) minNum = i;
}

console.log(minNum);