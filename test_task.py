from task import *


def test_todo_list():
    todo_list = TodoList("list")
    assert todo_list.tasks == []
    assert todo_list.number_of_tasks == 0

    task = Task('test', 'test', '2020-12-12')
    todo_list.add_task(task)
    assert todo_list.tasks == [task]
    assert todo_list.number_of_tasks == 1


class MockTodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)


def test_dispatcher():
    todo_list = MockTodoList()
    dispatcher = Dispatcher(todo_list)

    dispatcher.dispatch('test', 'test', '2020-12-12')

    assert len(todo_list.tasks) == 1
    assert todo_list.tasks[0].name == 'test'
    assert todo_list.tasks[0].description == 'test'
    assert todo_list.tasks[0].deadline == '2020-12-12'
