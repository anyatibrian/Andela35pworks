from time import strftime, gmtime


class Todo:
    def __init__(self):
        self.todo_list = []

    def add_task(self, name, created_at=strftime("%Y-%m-%d %H:%M:%S", gmtime())):
        """enables the user to add his or her task to the to do list"""
        dict_task = {
            'id': len(self.todo_list) + 1,
            'name': name,
            'create_at': created_at
        }
        self.todo_list.append(dict_task)
        return self.todo_list

    def show_task(self):
        """ show all the task in the todo list"""
        return self.todo_list

    def delete_task(self, todo_id):
        """delete the task from the todo list """
        if 0 < todo_id <= len(self.todo_list):
            task = [task for task in self.todo_list if task["id"] == todo_id]
            self.todo_list.remove(task[0])
        if not 0 < todo_id <= len(self.todo_list):
            return 'such an id does not exist'


class HomeTodo(Todo):
    def __init__(self, category):
        self.category = category
        self.todo_list = []

    def add_task(self, name, created_at=strftime("%Y-%m-%d %H:%M:%S", gmtime())):
        dict_task = {
            'id': len(self.todo_list) + 1,
            'name': name,
            'create_at': created_at,
            'category': self.category
        }
        self.todo_list.append(dict_task)
        return self.todo_list

    def show_single(self, task_id):
        """show single todo task """
        if 0 < task_id <= len(self.todo_list):
            tasks = [task for task in self.todo_list if task['id'] == task_id]
            return tasks[0]

        if not 0 < task_id <= len(self.todo_list):
            return 'such an id does not exist'


if __name__ == '__main__':

    hometodo = HomeTodo(category='playing pocka')
    hometodo.add_task(name='pock with my fried')
    hometodo.add_task(name='going to lira on monday')
    print(hometodo.show_single(2))
