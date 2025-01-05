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
# Turing3


def solution(k):
    # Peta karakter Romawi ke nilai Integer
    roman_to_int = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
    total = 0
    
    for i in range (len(k)) :
        if i < len(k) - 1 and roman_to_int[k[i]] < roman_to_int[k[i+1]] :
            total -= roman_to_int[k[i]]
        else :
            total += roman_to_int[k[i]]
            
    return total


# Input 
k = "MMDXLIX"

# Fungsi Hasil
result = solution(k)

# Output Hasil
print("Hasil : ",result)