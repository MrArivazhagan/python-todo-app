# from functions import get_todos, write_todos

from modules import functions
import time

print(time.strftime("%b %d, %Y %H:%M:%S"))

while True:
    user_need = input("Enter add, show, edit, complete or exit : ")
    user_need = user_need.strip()

    if user_need.startswith("add"):
        todo = user_need[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)
    elif user_need.startswith("show"):
        todos = functions.get_todos()

        # new_todos = [item.strip("\n") for item in todos]
        for index, todo in enumerate(todos):
            todo = todo.strip("\n")
            print(index+1, todo)
    elif user_need.startswith("edit"):
        try:
            input_index = int(user_need[5:])
            print(input_index)
            new_todo = input("Enter the new todo : ")

            todos = functions.get_todos()

            input_index -= 1
            todos[input_index] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Enter the todo's number you want to edit")
    elif user_need.startswith("complete"):
        try:
            input_index = int(user_need[9:])
            todos = functions.get_todos()

            todo_to_remove = todos[input_index-1]
            todo_to_remove = todo_to_remove.strip("\n")

            todos.pop(input_index-1)

            functions.write_todos(todos)
            print(f"Todo '{todo_to_remove}' is completed")
        except IndexError:
            print("There's no todo for the given number")
    elif "exit" in user_need:
        break
    else:
        print("Enter a valid command")

print("Bye!")

