from my_ui import write_line, in_txt

def repeat():
    while True:
        f = in_txt('ещё раз?\n')
        if f == 'y':
            simple_calc()
        elif f == 'n':
            write_line("Chao!")
            exit()
        else:
            write_line("Выберите "'y'" или "'n'"")