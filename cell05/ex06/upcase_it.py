#!/usr/bin/env python
import sys

# sys.argv ความยาวต้องเท่ากับ 2 เสมอ (ชื่อไฟล์ + 1 parameter)
# ถ้าเท่ากับ 2 แปลว่ามี Parameter มา 1 ตัวถูกต้อง
if len(sys.argv) == 2:
    # เอาตัวที่ 1 มาแปลงเป็นตัวใหญ่ (.upper()) แล้วปริ้น
    print(sys.argv[1].upper())
else:
    # ถ้าไม่เท่ากับ 2 (ไม่มี parameter หรือ มีมากกว่า 1)
    print("none")