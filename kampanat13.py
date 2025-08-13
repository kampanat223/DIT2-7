from datetime import datetime, date

def calculate_age(birthdate_str):
    # แปลง string เป็นวัตถุวันที่
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    today = date.today()

    # คำนวณอายุ
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    return age

# รับข้อมูลจากผู้ใช้
birthdate_input = input("กรุณาใส่วันเกิดของคุณ (รูปแบบ: YYYY-MM-DD): ")
try:
    age = calculate_age(birthdate_input)
    print(f"คุณมีอายุ {age} ปี")
except ValueError:
    print("YYYY-MM-DD")