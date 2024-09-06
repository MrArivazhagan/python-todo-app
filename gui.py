import functions
import FreeSimpleGUI as fsg
import time

fsg.theme('Black')

clock = fsg.Text('', key="clock")

label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter todo", key="todo")
add_button = fsg.Button(image_source='add.png', size=10,
                        mouseover_colors='blue', tooltip='Add Todo',
                        key='Add')

todos_list = fsg.Listbox(values=functions.get_todos(), key="todos",
                         size=(45, 10), enable_events=True)
edit_button = fsg.Button("Edit")

complete_button = fsg.Button(image_source='complete.png', size=(20, 10),
                             mouseover_colors='blue', tooltip='Complete Todo',
                             key='Complete')
exit_button = fsg.Button("Exit")

window = fsg.Window("To-do App",
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [todos_list, edit_button, complete_button],
                            [exit_button]],
                    font=('Helvetica', 20))

while True:
    # we put timeout to update the time in milliseconds
    event, values = window.read(timeout=100)
    print(event, values, sep="\n")
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            add_todo = values["todo"]
            if len(add_todo) == 0:
                continue
            todos.append(add_todo + "\n")
            functions.write_todos(todos)
            window["todos"].update(values=functions.get_todos())
        case "Edit":
            try:
                todos = functions.get_todos()
                edited_todo = values["todo"] + "\n"
                index = todos.index(values["todos"][0])
                todos[index] = edited_todo
                functions.write_todos(todos)
                # Accessing todos_list with it's key
                window["todos"].update(values=functions.get_todos())
            except IndexError:
                fsg.popup("Please Select a todo first", font=('Helvetica', 20))
        case "Complete":
            try:
                todos = functions.get_todos()
                index = todos.index(values["todos"][0])
                todos.pop(index)
                functions.write_todos(todos)
                window["todos"].update(values=functions.get_todos())
                # update in input box
                window["todo"].update(value="")
            except IndexError:
                fsg.popup("Please Select a todo first", font=('Helvetica', 20))
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=values["todos"][0].strip("\n"))
        # the close button click
        case fsg.WIN_CLOSED:
            break

window.close()
