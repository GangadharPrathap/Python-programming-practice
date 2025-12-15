class Project:
    def __init__(self, project_id, project_name):
        self.project_id = project_id
        self.project_name = project_name

class Module(Project):
    def __init__(self, project_id, project_name, module_name):
        super().__init__(project_id, project_name)
        self.module_name = module_name

class Task(Module):
    def __init__(self, project_id, project_name, module_name, task_name):
        super().__init__(project_id, project_name, module_name)
        self.task_name = task_name

    def display(self):
        print("Project Id:", self.project_id)
        print("Project Name:", self.project_name)
        print("Module Name:", self.module_name)
        print("Task Name:", self.task_name)

project_id = input("Enter Project id:\n")
project_name = input("Enter Project name:\n")
module_name = input("Enter Module name:\n")
task_name = input("Enter Task name:\n")

task_obj = Task(project_id, project_name, module_name, task_name)
task_obj.display()
