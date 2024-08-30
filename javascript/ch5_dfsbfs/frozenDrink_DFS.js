const fs = require('fs');
const path = require('path');
let input = fs
  .readFileSync(path.join(__dirname, 'test-drink.txt'))
  .toString()
  .trim()
  .split('\n');

let [nm, ...arr] = input;
const [n, m] = nm.split(' ').map((val) => Number(val));

function dfs(x, y, graph) {
  if (x <= -1 || x >= n || y <= -1 || y >= m) return;

  if (graph[x][y] === 0) {
    graph[x][y] = 1;

    dfs(x - 1, y, graph);
    dfs(x, y - 1, graph);
    dfs(x + 1, y, graph);
    dfs(x, y + 1, graph);
  }
}

function solution(n, m, arr) {
  const graph = arr.map((row) => row.split('').map((val) => Number(val)));

  let count = 0;

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (graph[i][j] === 0) {
        count += 1;
        dfs(i, j, graph);
      }
    }
  }

  return count;
}

console.log(solution(n, m, arr));
