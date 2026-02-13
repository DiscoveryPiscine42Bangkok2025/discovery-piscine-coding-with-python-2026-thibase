#!/usr/bin/env python
#  รับค่าตัวเลขทั้ง 2 ตัว
first_num = int(input("Give me the first number: "))
second_num = int(input("Give me the second number: "))

print("Thank you!")

# แสดงผลการคำนวณ (+, -, /, *)
print(str(first_num) + " + " + str(second_num) + " = " + str(first_num + second_num))
print(str(first_num) + " - " + str(second_num) + " = " + str(first_num - second_num))
print(str(first_num) + " / " + str(second_num) + " = " + str(first_num / second_num))
print(str(first_num) + " * " + str(second_num) + " = " + str(first_num * second_num))