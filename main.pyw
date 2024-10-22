from pynput import keyboard
from scripts import launch_program , minimize_window , overwolf_killer , window_manager , windows_cycle , alt_f4 , restore_window
import time

import subprocess

#program_path : str = "C:\\Program Files\\Git\\git-bash.exe"

last_execution_time = time.time()

pressed_now = set() 

good_keys = {'Key.alt_l','Key.f3','Key.enter','Key.home','Key.right','Key.left','Key.f4','Key.f5'}

last = time.time()

def on_press(key):
    global last
    time.sleep(0.01)
    keyy = str(key)
    global pressed_now
    if keyy not in good_keys:
        return
    if 'Key.alt_l' in pressed_now or keyy == 'Key.alt_l':
        pressed_now.add(keyy)
    print("on press " + str(pressed_now) + keyy)
    
    if time.time() - last > 0.2 and len(pressed_now) == 2:
        if 'Key.alt_l' in pressed_now and 'Key.f3' in pressed_now:
            last = time.time()
            minimize_window.minimize_focused_window()
            pressed_now = {'Key.alt_l'}
            print("executed minimization")

        elif 'Key.alt_l' in pressed_now and 'Key.enter' in pressed_now:
            last = time.time()
            #launch_program.launch_prompt(program_path)
            subprocess.Popen('start cmd', cwd='C:\\WINDOWS\\system32', shell=True)
            pressed_now = {'Key.alt_l'}
            print("executed bash")

        elif 'Key.alt_l' in pressed_now and 'Key.home' in pressed_now:
            last = time.time()
            window_manager.start_arranging()
            pressed_now = {'Key.alt_l'}
            print("executed arranging")

        elif 'Key.alt_l' in pressed_now and 'Key.right' in pressed_now:
            last = time.time()
            windows_cycle.focus_next_window()
            pressed_now = {'Key.alt_l'}
            print("executed focusing next")
            
        elif 'Key.alt_l' in pressed_now and 'Key.left' in pressed_now:
            last = time.time()
            windows_cycle.focus_previous_window()
            pressed_now = {'Key.alt_l'}
            print("executed focusing previous")

        elif 'Key.alt_l' in pressed_now and 'Key.f4' in pressed_now:
            last = time.time()
            pressed_now = {'Key.alt_l'}
            alt_f4.close_active_window()
            print("executed closing window")

        elif 'Key.alt_l' in pressed_now and 'Key.f5' in pressed_now:
            last = time.time()
            pressed_now = {'Key.alt_l'}
            restore_window.restore_focused_window()
            print("executed restoring window")

    global last_execution_time
    current_time = time.time()
    if current_time - last_execution_time > 600:
        last_execution_time = time.time()
        overwolf_killer.kill_overwolf()

def on_release(key):
    time.sleep(0.01)
    keyy = str(key)
    if keyy not in good_keys:
        return
    global pressed_now
    pressed_now.discard(keyy)
    print("on release " + str(pressed_now) + keyy)

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.canonical = True
listener.start()