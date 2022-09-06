from pynput import keyboard
from pynput.mouse import Button, Controller
from notifypy import Notify
import time

mouse = Controller()
click_position = (0, 0)
notification = Notify()

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    global click_position
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener        
        notification.title = "F5刷新后自动点击领题"
        notification.message = "程序已关闭"
        notification.send()
        return False
    elif key == keyboard.Key.f6:
        click_position = mouse.position
        print(click_position)
        notification.title = "F5刷新后自动点击领题"
        notification.message = "点击坐标已设置为 ({}, {})".format(*click_position)
        notification.send()
    elif key == keyboard.Key.f5:
        time.sleep(0.8)
        mouse.position = click_position
        mouse.click(Button.left, 1)


notification.title = "F5刷新后自动点击领题"
notification.message = "按 F6 设置当前位置为点击位置\n设置完成后按 F5 刷新并自动点击领题\n按 ESC 关闭程序".format(*click_position)
notification.send()

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
