#!/usr/bin/env python
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

#สร้างอาเรย์ใหม่ เฉพาะตัวที่ > 5 แล้วค่อยบวก 2
new_array = []
for num in original_array:
    if num > 5:
        new_array.append(num + 2)

# 3. แสดงผล
print(original_array)
print(new_array)