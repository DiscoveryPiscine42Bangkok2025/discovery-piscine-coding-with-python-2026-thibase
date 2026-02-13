#!/usr/bin/env python
# รับค่าและแปลงเป็น float (ทศนิยม) ทันที
num = float(input("Give me a number: "))

# เช็คว่าค่านั้น เป็นจำนวนเต็มหรือไม่ (เช่น 42.0 ถือเป็น integer)
if num.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")