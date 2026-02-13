#!/usr/bin/env python
# รับค่าตัวเลขที่ 1
first_num = int(input("Enter the first number:\n"))

# รับค่าตัวเลขที่ 2
second_num = int(input("Enter the second number:\n"))

# คำนวณผลคูณ
result = first_num * second_num

# แสดงประโยคการคูณ
print(str(first_num) + " x " + str(second_num) + " = " + str(result))

# ตรวจสอบผลลัพธ์ว่าเป็นบวก ลบ หรือ ศูนย์
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")