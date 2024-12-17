#importing necessary libraries
import json
import os
import datetime
import argparse
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

parser = argparse.ArgumentParser()

# Adding argument
parser.add_argument('-add', '--add', help='Fill the task to add', required=False)
parser.add_argument(
    '-list', '--list', help='type list "todo" or "in progress" or "done" or "all" for showing tasks', required=False)

parser.add_argument(
    '-update', '--update', help='Type new description', required=False)
parser.add_argument(
    '-mark', '--mark',action="append" , help='Type "in progress" or "done"', required=False)
parser.add_argument(
    '-delete', '--delete', help='Just type del', required=False)


# Processing argument
args = parser.parse_args()

# Accessing arguments
print(f'Added: {args.add if args.add else "No task added"}')
print(f'List: {args.list if args.list else "No list choosed"}')
# print(f'id: {args.pick if args.pick else "No id choosed"}')
print(f'update: {args.update if args.update else "Nothing updated"}')
print(f'mark: {args.mark if args.mark else "Nothing marked"}')
print(f'delete: {args.delete if args.delete else "Nothing marked"}')



#First getting the user input of the type of command
# inp_command = input("TaskCLI ")

#Getting the command from the input
# command = inp_command.split(" ")[0]

#Name of the file to check later if it exists or not
file_name = "database.json"

#Add Function if the user command is add, this function will add the task in the database
def add_command(context):
    #If the database file exists
    if os.path.exists(file_name):
        #then open it in read and write mode so that the previous data does not get omitted
        with open("database.json", "r+") as tasks:
            #Store the previous tasks in a data variable
            data = json.load(tasks)
            #Get the id of the last added task to get the next id for new task
            #if the database is empty then the new id is 1
            if data == []:
                new_id = 1
            #else the new id will be in increment to the last id in the database
            else:
                last_id = data[-1]["id"]
                new_id = last_id +1
            #Create the new data in JSON form
            new_data = {
                "id": new_id,
                "description": context,
                "status": "todo",
                "created_At": str(datetime.datetime.now()),
                "updated_At": "Not updated yet"
            }
            #Append the new task along the previous tasks in the data variable
            data.append(new_data)

            #Remove the previous data in the database so that it does not get repeated
            tasks.seek(0)
            tasks.truncate()
            #Add the updated data in the database (indent just gives indent in json to prettify the data)
            json.dump(data, tasks, indent=4)
        print(f"Task added successfully (ID: {new_id})")

    #If the database file does not exist (if this is the first task)
    else:
        #Create the data in json form to add in the database
        data = [{
            "id": 1,
            "description": context,
            "status": "todo",
            "created_At" : str(datetime.datetime.now()),
            "updated_At": "Not updated yet"
        }]
        #Open the file and add the data
        with open("database.json", "w") as tasks:
            json.dump(data, tasks, indent=4)

        print(f"Task added successfully (ID: {data[0]['id']})")

#Function to list all the tasks in the database
def list_all_tasks():
    if os.path.exists(file_name):
        with open("database.json", "r") as tasks:
            data = tasks.read()
    print(data)

#Function to delete a task with given id from the database
def delete_task(Id):
    if os.path.exists(file_name):
        with open("database.json", "r+") as tasks:
            data = json.load(tasks)
            # print(data)
            # print("    -    ")
            for item in data:
                if item["id"]==Id:
                    data.remove(item)
                    # print(data)
                    # break
                    tasks.seek(0)
                    tasks.truncate()
                    json.dump(data, tasks, indent=4)
                    return print(f"The task with Id:{Id} has been deleted from the database")
            print("This Id does not exists in the database")

    else:
        print("Database does not exists")


def update_task(Id, context):
    if os.path.exists(file_name):
        with open("database.json", "r+") as tasks:
            data = json.load(tasks)
            for item in data:
                if item["id"] == Id:
                    item["description"] = context
                    item["updated_At"] = str(datetime.datetime.now())

                    tasks.seek(0)
                    tasks.truncate()
                    json.dump(data, tasks, indent=4)
                    return print(f"Task with Id:{Id} has been updated")
            print("The given Id does not exist")
    else:
        print("Database does not exist.")


def mark_task(status, Id):
    if os.path.exists(file_name):
        with open("database.json", "r+") as tasks:
            data = json.load(tasks)
            for item in data:
                if item["id"] == Id:
                    item["status"] = status
                    item["updated_At"] = str(datetime.datetime.now())

                    tasks.seek(0)
                    tasks.truncate()
                    json.dump(data, tasks, indent=4)
                    return print(f"Status of the Task with Id:{Id} has been updated")
            print("The given Id does not exist")
    else:
        print("Database does not exist.")

def list_filter(status):
    if os.path.exists(file_name):
        list = []
        with open("database.json", "r+") as tasks:
            data = json.load(tasks)
            for item in data:
                if item["status"] == status:
                    list.append(item)
            if list:
                print(list)
            else:
                print(f"No tasks with status {status} found.")
    else:
        print("Database does not exist.")

# if command == "add":
#     context = inp_command.split(" ")[1]
#     add_command(context)
#
# if command == "list" and len(inp_command)== 4:
#     list_all_tasks()
#
# if command == "delete":
#     Id = inp_command.split(" ")[1]
#     # print(type(Id))
#     delete_task(int(Id))
#
# if command == "update":
#     Id = inp_command.split(" ")[1]
#     context = inp_command.split(" ")[2]
#     update_task(int(Id), context)
#
# if command.split("-")[0] == "mark":
#     Id = inp_command.split(" ")[1]
#     status = "-".join(command.split("-")[1:])
#     mark_task(status, int(Id))
#
# if command == "list" and len(inp_command)!= 4:
#     status = inp_command.split(" ")[1]
#     list_filter(status)

if args.add:
    add_command(args.add)

elif args.list:
    if str(args.list) == "all":
        list_all_tasks()
    else:
        list_filter(str(args.list))

elif args.delete:
    delete_task(int(args.delete))

elif args.mark:
    # print(args.mark)
    mark_task(args.mark[0], int(args.mark[1]))
