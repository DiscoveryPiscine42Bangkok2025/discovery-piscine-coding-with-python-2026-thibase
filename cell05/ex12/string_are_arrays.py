#!/usr/bin/env python
import sys

# 1. เช็คว่ามี parameter มา 1 ตัวถ้วนหรือไม่
if len(sys.argv) == 2:
    text = sys.argv[1]
    found_z = False  # สร้างตัวแปรมาจำว่า "เจอ z บ้างไหม?"
    
    # 2. วนลูปดูตัวอักษรทีละตัวในข้อความ
    for char in text:
        if char == 'z':
            print("z", end="")  # เจอ z ให้ปริ้น z (end="" คือไม่ขึ้นบรรทัดใหม่)
            found_z = True      # ติ๊กถูกว่าเจอแล้วนะ
            
    # 3. สรุปผลหลังจบลูป
    if found_z:
        print()       # ถ้าเจอ (ปริ้น z ไปบ้างแล้ว) ให้ปริ้นขึ้นบรรทัดใหม่ปิดท้าย
    else:
        print("none") # ถ้าวนจนจบแล้วไม่เจอ z เลย ให้ปริ้น none

else:
    # ถ้าจำนวน parameter ไม่ถูกต้อง
    print("none")