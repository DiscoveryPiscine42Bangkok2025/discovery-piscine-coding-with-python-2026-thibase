#!/usr/bin/env python
print("Enter a number less than 25")
# รับค่าตัวเลข
number = int(input())

# เช็คเงื่อนไข
if number > 25:
    print("Error")
else:
    # วนลูปจนกว่า number จะมากกว่า 25
    while number <= 25:
        print("Inside the loop, my variable is", number)
        number += 1  # บวกเลขเพิ่มทีละ 1