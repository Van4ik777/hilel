def roman_to_int(rom):
    roman = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
    }
    i = 0
    result = 0
    while i < len(rom):
        if i + 1 < len(rom) and rom[i:i+2] in roman:
            result += roman[rom[i:i+2]]
            i += 2  
        else:
            result += roman[rom[i]]
            i += 1 
    return result


def generate_hashtag(s):
    words = s.strip().split()
    
    if not words:
        return False
    
    hashtag = '#' + ''.join(word.capitalize() for word in words)
    
    return hashtag if 1 < len(hashtag) <= 140 else False