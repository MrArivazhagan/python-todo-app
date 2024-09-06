import FreeSimpleGUI as fsg
import convertor

label_text = fsg.Text("Convertor")

feet_label = fsg.Text("Enter feet ")
feet_input_box = fsg.Input(key="feet")

inch_label = fsg.Text("Enter inches ")
inch_input_box = fsg.Input(key="inches")

convert_button = fsg.Button("convert", key="convert")
output_text = fsg.Text(key="result")

window = fsg.Window(title="Convertor", layout=[[feet_label,feet_input_box],
                                        [inch_label, inch_input_box],
                                        [convert_button, output_text]])

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

