# Algorithm-practice

## Javascript

### 1) 한 줄에 공백으로 값이 들어올 때
```javascript
var input = require('fs').readFileSync('/dev/stdin').toString().split(' ');
var a = parseInt(input[0]);
var b = parseInt(input[1]);
```

### 2) 한 줄에 하나씩 값이 들어올 때
```javascript
var input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
```

## Python

### 1) N만큼 배열로 입력 받기
```python
N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]
```
