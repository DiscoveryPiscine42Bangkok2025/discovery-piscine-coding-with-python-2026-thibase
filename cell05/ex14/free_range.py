#!/usr/bin/env python
import sys

# 1. เช็คว่ามี Parameter มาครบ 2 ตัวหรือไม่ (รวมชื่อไฟล์เป็น 3)
if len(sys.argv) == 3:
    # 2. แปลงข้อความให้เป็นตัวเลข (Integer)
    start_num = int(sys.argv[1])
    end_num = int(sys.argv[2])
    
    # 3. สร้าง List จาก range
    # สูตรคือ range(ตัวเริ่ม, ตัวจบ + 1)
    # เพราะ Python จะหยุดก่อนถึงตัวจบเสมอ เราเลยต้องเผื่อไป 1 ตัว
    result_array = list(range(start_num, end_num + 1))
    
    # 4. แสดงผล
    print(result_array)
    
else:
    # ถ้า Parameter ไม่ครบ
    print("none")