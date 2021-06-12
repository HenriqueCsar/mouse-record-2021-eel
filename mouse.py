import eel, pyautogui, time

eel.init('gui')
global record
record = 0

@eel.expose
def positions_mouse():
    global record
    record = 1
    while record == 1:
        time.sleep(1)
        x = pyautogui.position()
        return x

@eel.expose
def change_options():
    global record
    record = 0


if __name__ == '__main__':
    eel.start('index.html')