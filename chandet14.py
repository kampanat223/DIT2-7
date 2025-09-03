"""
todo.py
โปรแกรมจัดการรายการงาน (To-Do List)
รองรับ: เพิ่มงาน, ลบงาน, แสดงงานทั้งหมด
"""

from typing import List

class TodoList:
    """คลาสจัดการรายการงาน"""

    def __init__(self):
        """สร้างรายการงานว่าง"""
        self.tasks: List[str] = []

    def add_task(self, task: str) -> None:
        """เพิ่มงานใหม่ลงในรายการ

        Args:
            task (str): งานที่ต้องการเพิ่ม
        """
        if not task.strip():
            raise ValueError("งานต้องไม่ว่าง")
        self.tasks.append(task)
        print(f"เพิ่มงาน: {task}")

    def remove_task(self, task: str) -> None:
        """ลบงานออกจากรายการ

        Args:
            task (str): งานที่ต้องการลบ
        """
        try:
            self.tasks.remove(task)
            print(f"ลบงาน: {task}")
        except ValueError:
            print(f"ไม่พบงาน: {task}")

    def show_tasks(self) -> None:
        """แสดงงานทั้งหมด"""
        if not self.tasks:
            print("ไม่มีงานในรายการ")
        else:
            print("รายการงานทั้งหมด:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")


if __name__ == "__main__":
    # ตัวอย่างการใช้งาน
    todo = TodoList()
    todo.add_task("ทำการบ้าน")
    todo.add_task("ซื้อของ")
    todo.show_tasks()
    todo.remove_task("ทำการบ้าน")
    todo.show_tasks()
