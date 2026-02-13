#!/usr/bin/env python
import sys

# 1. เช็คก่อนว่ามี parameter ส่งมาไหม (ต้องมากกว่า 1 เพราะตัวแรกคือชื่อไฟล์)
if len(sys.argv) > 1:
    # 2. วนลูปเช็คทีละคำ (เริ่มจากตัวที่ 1 จนจบ)
    for arg in sys.argv[1:]:
        # 3. เช็คว่าคำนี้ "ไม่ได้" ลงท้ายด้วย ism ใช่ไหม?
        if not arg.endswith("ism"):
            # ถ้าใช่ (ยังไม่มี ism) ให้เติม ism ต่อท้ายแล้วปริ้น
            print(arg + "ism")
        # ถ้าลงท้ายด้วย ism อยู่แล้ว โปรแกรมจะข้ามไปเอง (ไม่ทำอะไรในรอบนี้)
else:
    # ถ้าไม่มี parameter เลย
    print("none")