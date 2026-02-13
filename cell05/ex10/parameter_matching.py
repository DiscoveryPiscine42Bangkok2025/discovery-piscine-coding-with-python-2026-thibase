#!/usr/bin/env python
import sys

# 1. เช็คว่ามีการส่ง "คำลับ" มา 1 คำถ้วนหรือไม่
# (len ต้องเป็น 2 คือ ชื่อไฟล์ + คำลับ)
if len(sys.argv) == 2:
    
    # เก็บคำลับไว้ในตัวแปร (เอามาจาก parameter)
    secret = sys.argv[1]
    
    # 2. ถามผู้ใช้ให้พิมพ์ตอบ
    user_answer = input("What was the parameter? ")
    
    # 3. ตรวจคำตอบ (เทียบคำลับ กับ คำที่พิมพ์ตอบ)
    if secret == user_answer:
        print("Good job!")
    else:
        print("Nope, sorry...")
        
else:
    # กรณีไม่ได้ส่ง parameter มา หรือส่งมาเยอะเกิน
    print("none")