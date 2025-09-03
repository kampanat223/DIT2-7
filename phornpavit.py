from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB = "students.db"

# ฟังก์ชันเชื่อมต่อฐานข้อมูล
def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

# หน้าแสดงนักเรียนทั้งหมด
@app.route("/")
def index():
    conn = get_db()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("index.html", students=students)

# ฟอร์มแก้ไขข้อมูลนักเรียน
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_student(id):
    conn = get_db()

    if request.method == "POST":  # เมื่อกดปุ่มบันทึก
        name = request.form["name"]
        age = request.form["age"]
        grade = request.form["grade"]

        conn.execute(
            "UPDATE students SET name=?, age=?, grade=? WHERE id=?",
            (name, age, grade, id)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    student = conn.execute("SELECT * FROM students WHERE id=?", (id,)).fetchone()
    conn.close()
    return render_template("edit.html", student=student)

if __name__ == "__main__":
    app.run(debug=True)