#хазпхазпхазп я не можу як я це міг написати(я тоді ще не знав про хешмап)
def brackets(n: str) -> bool:
    '''
    checks if all brackets have open and close pair
    :param n: your str to sort
    :return: True if all  brackets in the string have an open and a closed pair .
    '''
    res = []
    opening = "([{"
    closing = ")]}"
    for i in n:
        if i in opening:
            res.append(i)
        elif i in closing:
            if not res:
                return False
            last = res.pop()
            if opening.index(last) != closing.index(i):
                return False
    return not res

def find_outlier(integers):
    more_odd = sum([num % 2 == 0 for num in integers[:3]]) >= 2
    
    if more_odd:
        for num in integers:
            if num % 2 != 0:
                return num
    else:
        for num in integers:
            if num % 2 == 0:
                return num