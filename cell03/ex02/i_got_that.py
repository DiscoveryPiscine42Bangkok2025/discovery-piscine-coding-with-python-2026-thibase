#!/usr/bin/env python
# 1. ถามคำถามแรกก่อนเริ่มวนลูป
user_input = input("What you gotta say? : ")

# 2. วนลูป ตราบใดที่ input ยัง "ไม่ใช่" คำว่า "STOP"
while user_input != "STOP":
    # ถามคำถามเดิมซ้ำๆ และเก็บค่าใหม่ใส่ตัวแปรเดิมเพื่อเอาไปเช็คในรอบต่อไป
    user_input = input("I got that! Anything else? : ")