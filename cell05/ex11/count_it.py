#!/usr/bin/env python
import sys

# 1. เช็คว่ามี parameter มาไหม (ต้องมากกว่า 1 เพราะ index 0 คือชื่อไฟล์)
if len(sys.argv) > 1:
    
    # 2. ปริ้นจำนวน parameter ทั้งหมดก่อน
    # (ลบ 1 ออก เพราะไม่นับชื่อไฟล์)
    print("parameters: " + str(len(sys.argv) - 1))
    
    # 3. วนลูปแสดงผลทีละตัว
    # sys.argv[1:] แปลว่า "เอาตั้งแต่ตัวที่ 1 ไปจนจบ" (ตัดตัวที่ 0 ทิ้ง)
    for param in sys.argv[1:]:
        # ปริ้น "คำ: ความยาว"
        print(param + ": " + str(len(param)))
        
else:
    # ถ้าไม่มี parameter
    print("none")