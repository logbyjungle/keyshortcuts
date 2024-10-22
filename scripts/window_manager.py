import pygetwindow as gw
import screeninfo
import ctypes

def arrange_windows_side_by_side(windows):
    screen_width = ctypes.windll.user32.GetSystemMetrics(0)
    screen_height = ctypes.windll.user32.GetSystemMetrics(1) - 42

    num_windows = len(windows)
    window_width = (screen_width // num_windows)

    for index, window in enumerate(windows):
        hwnd = window._hWnd
        
        ctypes.windll.user32.ShowWindow(hwnd, 1)
        
        x_position = index * window_width

        ctypes.windll.user32.MoveWindow(hwnd, x_position, 0, window_width, screen_height, True)

        ctypes.windll.user32.AllowSetForegroundWindow(ctypes.windll.kernel32.GetCurrentProcessId())
        
        ctypes.windll.user32.SetForegroundWindow(hwnd)

def start_arranging():
    height = screeninfo.get_monitors()[0].height - 40
    width = screeninfo.get_monitors()[0].width

    all_windows = [window for window in gw.getAllWindows() if window.title != '' and not (window.isMinimized or window.isMaximized) and window.title != 'Program Manager' and window.title != 'Microsoft Text Input Application']
    all_windows = [window for window in all_windows if window.height < height or window.width < width]

    if all_windows:
        for win in [window for window in gw.getAllWindows() if window.title != '' and window.title != 'Program Manager' and window.title != 'Microsoft Text Input Application' and (window.isMaximized or (window.height >= height and window.width >= width))]:
            win.minimize()

    if len(all_windows) == 0:
        print("no windows to arrange")
    elif len(all_windows) == 1:
        all_windows[0].maximize() 
    else:
        arrange_windows_side_by_side(all_windows)
        all_windows = [win.title for win in all_windows]
        print("arranged " + str(all_windows))

# non sempre tutte le finestre vengono portate in primo piano