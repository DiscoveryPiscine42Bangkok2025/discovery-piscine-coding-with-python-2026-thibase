#!/usr/bin/env python
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

#สร้างอาเรย์ใหม่ (ใช้ logic เดิม: เอาตัว > 5 แล้วบวก 2)
new_list = []
for num in original_array:
    if num > 5:
        new_list.append(num + 2)

#แปลง list ให้เป็น set เพื่อกำจัดตัวซ้ำ
new_set = set(new_list)

#แสดงผล
print(original_array)
print(new_set)