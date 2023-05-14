const fs = require('fs');
// const input = fs.readFileSync(__dirname + '/2738').toString().trim().split('\n');
let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const met = input.shift().split(" ").map(v => Number(v));

const a = [];
const b = [];

input.forEach((v, i) => i < met[0] ? a.push(v.split(" ").map(v => Number(v))) : b.push(v.split(" ").map(v => Number(v))))

a.map((e, i) => e.reduce((pre, cur, idx) => {
    pre.push(cur + b[i][idx])
    return pre;
  }, [])).forEach(v => console.log(v.join(" ")))