import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter todo")
add_button = fsg.Button("ADD")

window = fsg.Window("To-do App", layout=[[label], [input_box, add_button]])
window.read()
print("Window is closed")
window.close()