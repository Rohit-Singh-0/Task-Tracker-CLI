#importing necessary libraries
import argparse
from Tracker_functions import *
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
parser.add_argument('-a', '--add', help='Fill the task to add', required=False)
parser.add_argument(
    '-l', '--list', help='type list "todo" or "in progress" or "done" or "all" for showing tasks', required=False)

parser.add_argument(
    '-u', '--update', action="append", help='Type new description', required=False)
parser.add_argument(
    '-m', '--mark', action="append", help='Type "in progress" or "done" and the id of the task to mark in the next argument.', required=False)
parser.add_argument(
    '-d', '--delete', help='Just type del', required=False)


# Processing argument
args = parser.parse_args()

# Accessing arguments
print(f'Added: {args.add if args.add else "No task added"}')
print(f'List: {args.list if args.list else "No list choosed"}')
# print(f'id: {args.pick if args.pick else "No id choosed"}')
print(f'update: {args.update if args.update else "Nothing updated"}')
print(f'mark: {args.mark if args.mark else "Nothing marked"}')
print(f'delete: {args.delete if args.delete else "Nothing marked"}')


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

elif args.update:
    update_task(int(args.update[0]), str(args.update[1]))