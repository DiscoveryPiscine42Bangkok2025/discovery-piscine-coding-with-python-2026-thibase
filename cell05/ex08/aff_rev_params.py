#!/usr/bin/env python
import sys

# โจทย์บอกว่าต้องมี parameter อย่างน้อย 2 ตัว
# ดังนั้น len(sys.argv) ต้องมากกว่า 2 (ชื่อไฟล์ 1 + param 2 = 3)
if len(sys.argv) > 2:
    # วนลูปแบบถอยหลัง
    # range(จุดเริ่ม, จุดจบ, ขั้นบันได)
    # จุดเริ่ม: len(sys.argv) - 1 (คือตัวสุดท้าย)
    # จุดจบ: 0 (เพราะเราต้องการให้หยุดที่ 1, range จะหยุดก่อนถึงจุดจบเสมอ)
    # ขั้นบันได: -1 (ลดลงทีละ 1)
    for i in range(len(sys.argv) - 1, 0, -1):
        print(sys.argv[i])
else:
    print("none")