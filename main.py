numbers = []

# รับค่าจำนวน 5 จำนวนจากผู้ใช้
for i in range(5):
    num = int(input(f"ป้อนจำนวนตัวที่ {i+1}: "))
    numbers.append(num)

# เรียงลำดับจากน้อยไปมาก
numbers.sort()

# แสดงผลลัพธ์
print("ตัวเลขที่เรียงจากน้อยไปมากคือ:", numbers)
