#!/usr/bin/env python
import sys
import re  

# เช็คว่ามี Parameter มาครบ 2 ตัวไหม (รวมชื่อไฟล์เป็น 3)
if len(sys.argv) == 3:
    keyword = sys.argv[1]
    text = sys.argv[2]
    
    # ใช้ re.findall(สิ่งที่หา, แหล่งที่หา)
    # มันจะส่งค่ากลับมาเป็น List ของคำที่เจอทั้งหมด เช่น ['the', 'the']
    matches = re.findall(keyword, text)
    
    # เช็คว่าเจอไหม? (ถ้า List ไม่ว่าง แปลว่าเจอ)
    if len(matches) > 0:
        print(len(matches))  # ปริ้นจำนวนครั้งที่เจอ
    else:
        print("none")        # ถ้าไม่เจอเลย (List ว่าง) ให้ตอบ none
else:
    print("none")            # ถ้า Parameter ไม่ครบ ให้ตอบ none