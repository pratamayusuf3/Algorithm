
def BalanceDigit(k):
    
    for i in range (k-1, k//2, -1):
        if CalculateSum(1,i) == CalculateSum(i,k):
            return i
    return -1


def CalculateSum(start, end):
    n = end - start + 1
    return n * (start + end) // 2


def main():
    k = 49
    print("Hasil : ", BalanceDigit(k))


main()


