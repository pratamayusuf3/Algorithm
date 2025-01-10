# 3SumClosest - DONE
# ContainerMostWater - DONE
# LongestSubString - DONE
# ReverseInteger - DONE
# Turing1 - DONE

# 4Sum - DONE
# IntToRoman - DONE
# MedianTwoSortedArrays - DONE
# ReverseLetterOnly - DONE
# Turing2 - DONE

# AddLinkedList - DONE
# LetterComboOfPhone - DONE
# PalindromeNumber - DONE
# RomanToInt - DONE
# Turing3 - DONE

# BalanceDigit - DONE
# LongestComPrefix - DONE
# RegexMatch - DONE
# StrToInt -



def main():
    
    # Input
    s = "ab"
    p = ".*"
    
    # Fungsi Hasil
    result = solution(s,p)
    
    # Print Result
    print("Hasil : ", result)
    

def solution(s,p):    
    return match_helper(s,p,0,0)

def match_helper(s,p,i,j):
    if j == len(p):
        return i == len(s)
    
    match = i < len(s) and (s[i] == p[j] or p[j] == '.')
    
    if j+1 < len(p) and p[j+1] == '*':
        return match_helper(s,p,i,j+2) or (match and match_helper(s,p,i+1,j))
    else:
        return match and match_helper(s,p,i+1,j+1)
        
    
# Menjalankan fungsi utama 
if __name__ == "__main__":
    main()