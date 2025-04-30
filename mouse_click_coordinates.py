import pyautogui
import pynput


def on_click(x, y, button, pressed):
    if pressed:
        print(f'鼠标点击位置坐标: ({x}, {y})')


with pynput.mouse.Listener(on_click=on_click) as listener:
    listener.join()