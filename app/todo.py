class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")
        task = {"title": title.strip(), "done": False}
        self.tasks.append(task)
        return task

    def complete_task(self, index):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task index out of range")
        self.tasks[index]["done"] = True

    def remove_task(self, index):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task index out of range")
        return self.tasks.pop(index)

    def get_pending(self):
        return [t for t in self.tasks if not t["done"]]

    def get_completed(self):
        return [t for t in self.tasks if t["done"]]

    def count(self):
        return len(self.tasks)
