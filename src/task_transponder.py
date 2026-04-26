# Task Transponder Module
# Handles Apex Cell task metadata

class TaskTransponder:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        """Add a new task to the Apex Cell."""
        task = {
            'description': description,
            'state': 'TODO'
        }
        self.tasks.append(task)
        print(f"Task added: {description}")

    def review_tasks(self):
        """Review and process tasks."""
        print("Reviewing tasks:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task['description']} (State: {task['state']})")

    def process_task(self, task_index):
        """Mark a task as processed."""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['state'] = 'PROCESSED'
            print(f"Task {task_index + 1} processed.")
        else:
            print("Invalid task index.")