import json
#This is the Task Tracker CLI

'''
Requirements
The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

Add, Update, and Delete tasks
Mark a task as in progress or done
List all tasks
List all tasks that are done
List all tasks that are not done
List all tasks that are in progress
Here are some constraints to guide the implementation:

You can use any programming language to build this project.
Use positional arguments in command line to accept user inputs.
Use a JSON file to store the tasks in the current directory.
The JSON file should be created if it does not exist.
Use the native file system module of your programming language to interact with the JSON file.
Do not use any external libraries or frameworks to build this project.
Ensure to handle errors and edge cases gracefully.
'''

#Creating a class Task Tracker
class TaskTracker:
    #creating the add task function to add a new task
    def add_task(self,task_id,task,task_details,task_date, tasks):
        self.details = {
            task_id:{
                "Task":task,
                "Task Details":task_details,
                "Task Deadline":task_date
            }
        }
        return json.dumps(self.details)

    def update_task(self, task_id,upd_task, upd_task_details, upd_task_date, tasks):
        if task_id in tasks:
            if upd_task:
                tasks[task_id]["Task"] = upd_task
            if upd_task_details:
                tasks[task_id]["Task Details"] = upd_task_details
            if upd_task_date:
                tasks[task_id]["Task Deadline"] = upd_task_date

            return tasks
        else:
            return "Task ID does not exists."

tasks = open("tasks_record.txt", 'w')

manager = TaskTracker()
p = manager.add_task(task_id='1',task="Study", task_details="Complete Unit 1 of CN", task_date="29 August 2024", tasks=tasks)
print(p)
