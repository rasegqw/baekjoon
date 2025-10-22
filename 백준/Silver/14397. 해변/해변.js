const fs = require("fs")

const input = fs.readFileSync(0, "utf8").trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);

let world = Array.from({length:N}, () => Array(M).fill(false));

for (let i = 0; i<N; i++) {
    const row = input[i+1].split("")
    
    for (let j = 0 ; j<M; j++) {
        if (row[j] == '#') world[i][j] = true;
    }
}

let cnt = 0;

for (let i = 0; i<N-1; i++) {
    const row = world[i]
    const nextRow = world[i+1]

    for (let j = 0; j<M-1; j++) {
        if (row[j] != row[j+1]) cnt++;
    }

    if (i % 2 == 0) {
        if (row[0] != nextRow[0]) cnt++;

        for (let j = 1; j<M; j++) {
            if (row[j] != nextRow[j]) cnt++;
            if (row[j] != nextRow[j-1]) cnt++;
        }   
    } else {
        for (let j = 0; j<M-1; j++) {
            if (row[j] != nextRow[j+1]) cnt++;
            if (row[j] != nextRow[j]) cnt++;
        }

        if (row[M-1] != nextRow[M-1]) cnt++;
    }
}

const row = world[N-1];
for (let j = 0; j<M-1; j++) {
    if (row[j] != row[j+1]) cnt++;
}


console.log(cnt)