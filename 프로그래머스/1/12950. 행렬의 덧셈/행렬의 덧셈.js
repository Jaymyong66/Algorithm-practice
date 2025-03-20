function solution(arr1, arr2) {
    var answer = [];
    
    arr1.forEach((row, i) => {
        const _row = [];
        
        row.forEach((char, j) => {
            _row.push(char + arr2[i][j]);
        })
        answer.push(_row);
    })
    return answer;
}