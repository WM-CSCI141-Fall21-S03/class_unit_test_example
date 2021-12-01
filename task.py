class Task:
    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline


class TodoList:

    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.number_of_tasks = 0

    def add_task(self, task):
        self.tasks.append(task)
        self.number_of_tasks += 1


class Dispatcher:

    def __init__(self, todo_list):
        self.todo_list = todo_list

    def dispatch(self, name, description, deadline):
        self.todo_list.add_task(Task(name, description, deadline))
