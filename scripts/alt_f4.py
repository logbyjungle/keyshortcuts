import pygetwindow as gw
from pywinauto import Application

def close_active_window():
    active_window = gw.getActiveWindow()

    if active_window and active_window.title != '' and not active_window.isMinimized and active_window.title != 'Program Manager' and active_window.visible and active_window.title != 'Microsoft Text Input Application':
        app = Application().connect(handle=active_window._hWnd)
        app.window(handle=active_window._hWnd).close()
        print(f"Closed window: {active_window.title}")
    else:
        print("No active window found.")