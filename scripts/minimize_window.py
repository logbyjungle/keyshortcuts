import pygetwindow as gw

def minimize_focused_window():
    active_window = gw.getActiveWindow()
    print("----------------")
    if active_window is not None:
        print(active_window.title)
        active_window.minimize()

        # all_windows = [window for window in gw.getAllWindows() if window.title != '' and not window.isMinimized and window.title != 'Program Manager' and window.visible and window.title != 'Microsoft Text Input Application']
        # print([window.title for window in all_windows])

        # for window in all_windows:
        #     window.minimize()
        #     window.restore()
        #     print(f"Should've Activated trough restore window: {window.title}")