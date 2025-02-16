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
# Turing3 - 

# BalanceDigit - DONE
# LongestComPrefix - DONE
# RegexMatch - DONE
# StrToInt - DONE
# TwoSum - DONE

# BinaryDepth - DONE
# LongestPalindromSubstring - DONE
# RemoveNthNode -
# ThreeSum - DONE
# ZigZag - DONE


def solution(s):
    # Peta karakter Romawi ke nilai Integer
    roman_to_int = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
    result = 0
    
    for i in range (len(s)):
        if i < len(s) - 1 and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
            result -= roman_to_int[s[i]]
        else:
            result += roman_to_int[s[i]]
            
    return result





# Input 
k = "MMDXLIX"

# Fungsi Hasil
result = solution(k)

# Output Hasil
print("Hasil : ",result)
