def find_substrings(a1, a2):
    result = [word for word in a1 if any(word in word2 for word2 in a2)]

    return sorted(result)


def high_and_low(numbers):
    num_list = [int(num) for num in numbers.split()]
    
    highest = max(num_list)
    lowest = min(num_list)
    
    return f"{highest} {lowest}"


def row_sum_odd_numbers(n):
    first = n**2 - (n - 1)
    
    row = first
    
    for _ in range(n - 1):
        first += 2
        row += first
        
    return row


def high_and_low(numbers):
    num_list = [int(num) for num in numbers.split()]
    
    highest = max(num_list)
    lowest = min(num_list)
    
    return f"{highest} {lowest}"


def count_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def new_format(string): 
    res = [] 
    res+=''.join(reversed(string))
    i= 0 
    for i in range(len(res)):
        i += 1 
        if i % 3 == 0: res[i] +=(',')
        res.reverse()
        result ="" 
        for i in range(len(res)):
            result += res[i] 
    return result


def to_camel_case(s):
    parts = s.replace('_', '-').split('-')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])