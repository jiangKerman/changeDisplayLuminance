# pip install monitorcontrol
# pip install pynput

from monitorcontrol import get_monitors
from pynput import keyboard

monitors = get_monitors()
with monitors[0] as monitor:
    luminance = monitor.get_luminance()

print("用方向键↑ ↓调整亮度，esc退出")


def on_press(key):
    global luminance
    if key == keyboard.Key.up:
        # 按下 ↑ 亮度加10
        for monitor in monitors:
            with monitor:
                if (luminance + 10) > 100:
                    monitor.set_luminance(100)
                    luminance = 100
                else:
                    monitor.set_luminance(luminance + 10)
                    luminance += 10
                print("亮度:" + str(luminance))

    if key == keyboard.Key.down:
        # 按下 ↓ 亮度减10
        for monitor in monitors:
            with monitor:
                if (luminance - 10) < 0:
                    monitor.set_luminance(0)
                    luminance = 0
                else:
                    monitor.set_luminance(luminance - 10)
                    luminance -= 10
                print("亮度:" + str(luminance))
    if key == keyboard.Key.esc:
        return False


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
