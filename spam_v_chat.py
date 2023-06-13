import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

time.sleep(5)

x = 1000
while x > 0:
    keyboard.type(str(x)+"-7="+str(x-7))
    x -= 7
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.01)

keyboard.press(Key.enter)
keyboard.release(Key.enter)
