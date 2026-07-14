import json
import os

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def save_tasks(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, title):
        self.tasks.append({"title": title, "completed": False})
        self.save_tasks()
        print(f"Завдання '{title}' додано.")

    def list_tasks(self):
        if not self.tasks:
            print("Список завдань порожній.")
            return
        for i, task in enumerate(self.tasks):
            status = "[x]" if task["completed"] else "[ ]"
            print(f"{i + 1}. {status} {task['title']}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()
            print("Завдання позначено як виконане.")
        else:
            print("Невірний індекс завдання.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"Завдання '{removed['title']}' видалено.")
        else:
            print("Невірний індекс завдання.")

def main():
    manager = TaskManager()
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Показати завдання")
        print("2. Додати завдання")
        print("3. Виконати завдання")
        print("4. Видалити завдання")
        print("5. Вихід")
        
        choice = input("Оберіть опцію: ")
        
        if choice == '1':
            manager.list_tasks()
        elif choice == '2':
            title = input("Введіть назву завдання: ")
            manager.add_task(title)
        elif choice == '3':
            manager.list_tasks()
            idx = int(input("Номер завдання для виконання: ")) - 1
            manager.complete_task(idx)
        elif choice == '4':
            manager.list_tasks()
            idx = int(input("Номер завдання для видалення: ")) - 1
            manager.delete_task(idx)
        elif choice == '5':
            print("До побачення!")
            break
        else:
            print("Спробуйте ще раз.")

if __name__ == "__main__":
    main()
