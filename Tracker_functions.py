import json
import datetime
import os


#Name of the file to check later if it exists or not
file_name = "database.json"

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