import FreeSimpleGUI as fsg
import convertor

label_text = fsg.Text("Convertor")

feet_label = fsg.Text("Enter feet ")
feet_input_box = fsg.Input(key="feet")

inch_label = fsg.Text("Enter inches ")
inch_input_box = fsg.Input(key="inches")

convert_button = fsg.Button("convert", key="convert")
output_text = fsg.Text(key="result")

left_column_content = [[feet_label],
                       [inch_label],
                       [convert_button]]

right_column_content = [[feet_input_box],
                        [inch_input_box],
                        [output_text]]

left_column = fsg.Column(layout=left_column_content)
right_column = fsg.Column(layout=right_column_content)

layout = [[left_column, right_column]]

window = fsg.Window(title="Convertor", layout=layout)

while True:
    event, values = window.read()
    print(event, values, sep='\n')
    match event:
        case "convert":
            feet = float(values["feet"])
            inches = float(values["inches"])
            meters = convertor.convert(feet, inches)
            window['result'].update(value=f"{meters} m")
        case fsg.WIN_CLOSED:
            break

window.close()

