def solution(binTree):
    
    # validasi 0
    if len(binTree) == 0 or binTree[0] is None :
        return 0
    
    queue = [0]  # memulai dari akar index 0
    depth = 0
    
    while queue :
        level_size = len(queue)     # jumlah node saat ini
        depth += 1
        
        # menelusuri semua node saat ini
        for i in range (level_size):
            index = queue.pop(0)    # ambil elemen pertama dari queue
            
            # anak kiri jika ada dalam indeks
            left_child_idx = 2 * index + 1
            if left_child_idx < len(binTree) and binTree[left_child_idx] is not None:
                queue.append(left_child_idx)
                
            # anak kanan jika ada dalam indeks
            right_child_idx = 2 * index + 2
            if right_child_idx < len(binTree) and binTree[right_child_idx] is not None :
                queue.append(right_child_idx)
                
    return depth


# input
k = ["1", "9", "29", None, None, "15", "7"]

# output
result = solution(k)
print("Hasil : ", result)
            
            