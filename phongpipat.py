def get_user_info():
    name = input("กรุณากรอกชื่อ: ")
    age = input("กรุณากรอกอายุ: ")
    gender = input("กรุณากรอกเพศ (ชาย/หญิง/อื่น ๆ): ")
    
    user_info = {
        "ชื่อ": name,
        "อายุ": age,
        "เพศ": gender
    }
    
    return user_info

def main():
    info = get_user_info()
    print("\nข้อมูลผู้ใช้:")
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
