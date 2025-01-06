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

# BalanceDigit -


def solution(k):
    # jumlah total selisih absolut antara digit angka-angka pada semua pasangan elemen array
    
    total = 0
    
    for i in range (len(k)-1) :
        for j in range (i+1, len(k),1):
            temp1 = k[i]
            temp2 = k[j]
            
            while temp1 > 0 and temp2 > 0 :
                digit1 = temp1 % 10
                digit2 = temp2 % 10
                total += abs(digit1 - digit2)
                temp1 = temp1 // 10
                temp2 = temp2 // 10
                
    return total
            

# Input
k = [23, 13, 14]

# Output 
result = solution(k)

# Print result
print("Hasil : ",result)