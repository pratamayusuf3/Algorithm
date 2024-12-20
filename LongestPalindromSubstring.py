def solution(s):
    
    if not s or len(s) < 1:
        return ""
    
    result = ""
    max_length = 0
    
    for i in range(len(s)):
        
        odd_palindrome = expand_center(s,i,i)
        
        even_palindrome = expand_center(s,i,i+1)
        
        if len(odd_palindrome) > max_length:
            result = odd_palindrome
            max_length = len(odd_palindrome)
            
        if len(even_palindrome) > max_length:
            result = even_palindrome
            max_length = len(even_palindrome)
        
    return result


def expand_center(s,left,right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]


input_str = "babad"

result = solution(input_str)

print("Hasil : ", result)
    