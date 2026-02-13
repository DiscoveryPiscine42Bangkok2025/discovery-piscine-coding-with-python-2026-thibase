#!/usr/bin/env python
import sys

# เช็คว่ามี Parameter มา 1 ตัวถ้วนหรือไม่ (รวมชื่อไฟล์เป็น 2)
if len(sys.argv) == 2:
    # แปลงเป็นตัวพิมพ์เล็ก (.lower()) แล้วปริ้น
    print(sys.argv[1].lower())
else:
    # ถ้าไม่ใช่ ให้ปริ้น none
    print("none")