#!/usr/bin/env python
print("Enter a number")
number = int(input())

# วนลูปตั้งแต่ 0 ถึง 9 (range(10) คือ 0,1,2...9)
for i in range(10):
    result = i * number
    print(str(i) + " x " + str(number) + " = " + str(result))