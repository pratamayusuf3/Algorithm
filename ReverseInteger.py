def solution(x):
    reversed_number = 0
    
    while x != 0:
        digit = x % 10 if x > 0 else x % -10
        x = x // 10
        
        # Validasi Overflow
        if (reversed_number > (2**31 -1) // 10 or (reversed_number == (2**31 - 1) // 10 and digit > 7)):
            return 0
        if (reversed_number < -2**31 // 10 or (reversed_number == -2**31 // 10 and digit < -8)):
            return 0
        
        reversed_number = reversed_number * 10 + digit
        
    return reversed_number


def solution2(x):
    reversed_number = 0
    
    while x != 0:
        digit = x % 10 if x > 0 else x % -10
        x = x // 10
        
        reversed_number  = reversed_number * 10 + digit
        
        # Validasi Overflow / ini kemungkinan bisa di python karena tipe data otomatis di python
    if reversed_number > 2**31 - 1 or reversed_number < -2**31:
        return 0

    return reversed_number


if __name__ == "__main__":
    x = 12345
    print("Hasil:", solution(x))
    print("Hasil 2 :", solution2(x))  #ini kemungkinan bisa di python karena tipe data otomatis di python
    print("Test Mod Negatif 1 : ", -12345 % -10)
    print("Test Mod Negatif 2 : ", -12345 % 10)
        