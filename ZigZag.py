def zigzag1(s, num_rows):
    if num_rows == 1 or num_rows >= len(s):
        return s
    
    # Buat daftar untuk setiap baris
    rows = [""] * num_rows
    current_row = 0
    going_down = False
    
    # Iterasi melalui karakter di string
    for c in s:
        rows[current_row] += c
        
        # ubah arah turun atau naik
        if current_row == 0 or current_row == num_rows - 1:
            going_down = not going_down
            
        # tambah jika turun, kurangi jika naik
        # current_row += 1 if going_down else - 1
        
        if going_down:
            current_row += 1
        else:
            current_row -= 1
        
    # Gabungkan hasil
    return "".join(rows)


def zigzag2 (s, num_rows):
    if num_rows <= 1 or num_rows > len(s):
        return s
    
    # Buat daftar untuk setiap baris
    rows = [[] for _ in range(num_rows)]
    cur_pos = 0
    up_down = 1
    
    # Iterasi melalui karakter di string
    for c in s:
        rows[cur_pos].append(c)
        if cur_pos == 0:
            up_down = 1
        elif cur_pos == num_rows - 1:
            up_down = -1
        cur_pos += up_down
        
    # Gabungkan hasil
    result = []
    for row in rows:
        result.extend(row)

    return "".join(result)


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    num_rows = 3
    
    result = zigzag1(s, num_rows)
    result2 = zigzag2(s, num_rows)
    
    print("result : ", result)
    print("result2 : ", result2)