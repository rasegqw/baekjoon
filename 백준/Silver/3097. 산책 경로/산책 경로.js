const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split("\n")

// console.log(input)
const N = Number(input[0]);

let routes = Array.from({ length: N }, () => new Array(2));

let cur_x = 0;
let cur_y = 0;

// console.log(routes);

for (let i = 1; i<=N; i++) {
    const [x, y] = input[i].split(" ").map(Number);
    
    routes[i-1][0] = x;
    routes[i-1][1] = y;
    
    cur_x += x;
    cur_y += y;
}

console.log(cur_x, cur_y);

let minAns = 1<<30;

for (let i = 0; i<N; i++) {
    const res = getDistance(cur_x-routes[i][0], cur_y-routes[i][1]);

    minAns = Math.min(minAns, res);
}

console.log(minAns.toFixed(2));

function getDistance(x, y) {
    const total = x*x + y*y;
    return Math.sqrt(total);    
}