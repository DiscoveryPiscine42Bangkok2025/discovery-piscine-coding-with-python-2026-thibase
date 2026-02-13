#!/usr/bin/env python
# กำหนดรหัสผ่านที่ถูกต้องตามโจทย์
correct_password = "Python is awesome"

# รอรับรหัสผ่านจากผู้ใช้
user_input = input()

# ตรวจสอบว่าตรงกันไหม
if user_input == correct_password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")