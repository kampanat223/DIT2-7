# สร้าง list สำหรับเก็บข้อมูลนักเรียน
students = []

# ฟังก์ชันเพิ่มข้อมูลนักเรียน
def add_student():
    print("\n=== เพิ่มข้อมูลนักเรียน ===")
    student_id = input("รหัสนักเรียน: ")
    name = input("ชื่อนักเรียน: ")
    age = input("อายุ: ")
    grade = input("ชั้นปี/ระดับชั้น: ")

    # สร้าง dictionary สำหรับเก็บข้อมูลของนักเรียนคนนี้
    student = {
        "รหัส": student_id,
        "ชื่อ": name,
        "อายุ": age,
        "ชั้นปี": grade
    }

    # เพิ่มนักเรียนเข้า list
    students.append(student)
    print("✅ เพิ่มข้อมูลนักเรียนเรียบร้อยแล้ว!\n")

# ฟังก์ชันแสดงนักเรียนทั้งหมด
def show_students():
    print("\n=== รายชื่อนักเรียนทั้งหมด ===")
    if not students:
        print("ยังไม่มีข้อมูลนักเรียน\n")
    else:
        for i, student in enumerate(students, start=1):
            print(f"{i}. รหัส: {student['รหัส']} | ชื่อ: {student['ชื่อ']} | อายุ: {student['อายุ']} | ชั้นปี: {student['ชั้นปี']}")
        print()

# เมนูหลัก
def main_menu():
    while True:
        print("=== ระบบจัดการข้อมูลนักเรียน ===")
        print("1. เพิ่มข้อมูลนักเรียน")
        print("2. แสดงรายชื่อนักเรียนทั้งหมด")
        print("3. ออกจากโปรแกรม")
        choice = input("เลือกเมนู (1-3): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            print("👋 ออกจากโปรแกรมแล้ว")
            break
        else:
            print("❌ กรุณาเลือกเมนูให้ถูกต้อง (1-3)\n")

# เรียกใช้งานเมนูหลัก
main_menu()
