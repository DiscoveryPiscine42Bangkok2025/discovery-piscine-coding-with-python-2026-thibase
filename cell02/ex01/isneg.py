#!/usr/bin/env python
# รับค่าและแปลงเป็นตัวเลข
number = int(input())

# ตรวจสอบเงื่อนไข
if number < 0:
    print("This number is negative.")
elif number > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")