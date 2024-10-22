import pygetwindow as gw
import screeninfo

def restore_focused_window():
    active_window = gw.getActiveWindow()
    height = screeninfo.get_monitors()[0].height - 40
    width = screeninfo.get_monitors()[0].width
    if active_window:
        #if active_window.height >= height and active_window.width >= width:
        if active_window.isMaximized:
            if active_window.title != '' and active_window.title != 'Program Manager' and active_window.title != 'Microsoft Text Input Application':
                active_window.restore()
                print("restored window " + str(active_window.title))