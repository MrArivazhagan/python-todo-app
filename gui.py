import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter todo", key="todo")
add_button = fsg.Button("Add")

todos_list = fsg.Listbox(values=functions.get_todos(), key="todos",
                         size=(45, 10), enable_events=True)
edit_button = fsg.Button("Edit")

complete_button = fsg.Button("Complete")
exit_button = fsg.Button("Exit")

window = fsg.Window("To-do App",
                    layout=[[label],
                            [input_box, add_button],
                            [todos_list, edit_button, complete_button],
                            [exit_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event, values, sep = "\n")

    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.write_todos(todos)
            window["todos"].update(values=functions.get_todos())
        case "Edit":
            todos = functions.get_todos()
            edited_todo = values["todo"] + "\n"
            index = todos.index(values["todos"][0])
            todos[index] = edited_todo
            functions.write_todos(todos)
            # Accessing todos_list with it's key
            window["todos"].update(values=functions.get_todos())
        case "Complete":
            todos = functions.get_todos()
            index = todos.index(values["todos"][0])
            todos.pop(index)
            functions.write_todos(todos)
            window["todos"].update(values=functions.get_todos())
            # update in input box
            window["todo"].update(value="")
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=values["todos"][0].strip("\n"))
        # the close button click
        case fsg.WIN_CLOSED:
            break

window.close()