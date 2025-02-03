# 3SumClosest - DONE
# ContainerMostWater - DONE
# LongestSubString - DONE
# ReverseInteger - 
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
# StrToInt - DONE
# TwoSum - DONE

# BinaryDepth - DONE
# LongestPalindromSubstring - DONE
# RemoveNthNode -
# ThreeSum - DONE
# ZigZag - DONE



def solution(s):
    left = 0
    set_sub = set()
    max_sub = 0
    
    
    for right in range (len(s)):
        if s[right] not in set_sub:
            set_sub.add(s[right])
            max_sub = max(max_sub,right - left + 1)
        else:
            while s[right] in set_sub:
                set_sub.remove(s[left])
                left += 1
    return max_sub
            


# Test Case
test_str = "abcbcbb"
result = solution(test_str)

# Menampilkan Hasil
print("Hasil : ", result)
