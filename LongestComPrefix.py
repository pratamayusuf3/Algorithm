def solution(v):
    
    v.sort()
    
    first = v[0]
    print("first : ", first)
    
    last = v[-1]
    print("last : ", last)
    
    last2 = v[len(v)-1]
    print("last2 : ", last2)
    
    ans = []
    
    for i in range (min(len(first),len(last))):
        if first[i] != last[i]:
            return "".join(ans)
        ans.append(first[i])
        
    return "".join(ans)


# Input
v = ["flower", "flow", "flight"]

# Output
result = solution(v)

# Print Result
print("Hasil : ", result)