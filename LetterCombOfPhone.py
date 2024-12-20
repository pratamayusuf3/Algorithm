# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

def letterCombination(digits):
    dict_1 = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    
    if not digits:
        return []
      
    result = [""]
    
    for x in digits:
        temp = []
        for a in result:
            for j in dict_1[x]:
                temp.append(a + j)
        result = temp
    
    return result


if __name__ == "__main__":
    digits = "23"
    
    result = letterCombination(digits)
    
    print("Hasil : ", result)