def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        row = ''
        bit_result = bin(arr1[i] | arr2[i])[2:]
        
        if len(bit_result) < n:
           bit_result = (n - len(bit_result)) * '0' + bin(arr1[i] | arr2[i])[2:]
        
        for bit in bit_result:
            if bit == '1':
                row += '#'
            else:
                row += ' '

        answer.append(row)
        
    return answer