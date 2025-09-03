# รายการข้อมูลนักเรียน (แต่ละคนเป็น dictionary)
students = [
    {"id": "001", "name": "สมชาย"},
    {"id": "002", "name": "สมหญิง"},
    {"id": "003", "name": "ประยุทธ"}
]

# ฟังก์ชันลบข้อมูลตามรหัสนักเรียน
def delete_student(student_id):
    global students
    original_length = len(students)
    students = [s for s in students if s["id"] != student_id]
    
    if len(students) < original_length:
        print(f"ลบนักเรียนรหัส {student_id} เรียบร้อยแล้ว")
    else:
        print(f"ไม่พบนักเรียนรหัส {student_id}")

# ทดลองลบ
delete_student("002")

# แสดงรายชื่อนักเรียนหลังลบ
print("รายชื่อนักเรียนที่เหลือ:")
for s in students:
    print(f"{s['id']} - {s['name']}")
