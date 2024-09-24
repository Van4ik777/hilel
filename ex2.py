def solution(s):
    result = []
    for char in s:
        if char.isupper() and result:
            result.append(' ')  
        result.append(char)
    return ''.join(result) 

def move_zeros(arr):
    result = [x for x in arr if x is not None and x != 0]
    result.extend([0] * (len(arr) - len(result)))
    return result

def is_prime(n):

    if n <= 1:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
        
    return True