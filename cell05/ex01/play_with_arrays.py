#!/usr/bin/env python
# 1. สร้างอาเรย์ต้นฉบับ (ใช้เลขตามโจทย์)
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# 2. สร้างอาเรย์ใหม่ โดยเอาสมาชิกทุกตัวใน original มาบวก 2
new_array = []
for num in original_array:
    new_array.append(num + 2)

# 3. แสดงผล
print("Original array:", original_array)
print("New array:", new_array)