#!/usr/bin/env python
import sys

# เช็คว่ามี parameter ส่งมาหรือเปล่า? 
# (ต้องมากกว่า 1 เพราะตัวที่ 0 คือชื่อไฟล์)
if len(sys.argv) > 1:
    # ถ้ามี ให้ปริ้นตัวที่ 1 (parameter ตัวแรก)
    print(sys.argv[1])
else:
    # ถ้าไม่มี ให้ปริ้น none
    print("none")