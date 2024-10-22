import pygetwindow as gw
import screeninfo
import ctypes

# Function to check if a window is covered by another
def is_fully_covered(target_window, other_windows):
    target_left, target_top = target_window.left, target_window.top
    target_right, target_bottom = target_left + target_window.width, target_top + target_window.height

    for other_window in other_windows:
        if other_window == target_window:
            continue
        
        other_left, other_top = other_window.left, other_window.top
        other_right, other_bottom = other_left + other_window.width, other_top + other_window.height
        
        # Check if the other window completely covers the target window
        if (other_left <= target_left and other_top <= target_top and
            other_right >= target_right and other_bottom >= target_bottom):
            return True
    
    return False

def focus_next_window():
    ctypes.windll.user32.AllowSetForegroundWindow(ctypes.windll.kernel32.GetCurrentProcessId())
    windows = getwindows()
    if len(windows) >= 2:
        focused_index = next((i for i, (w, f) in enumerate(windows) if f == 1), None)
        windows = getwindows()
        if focused_index is not None and focused_index < len(windows) - 1:
            next_index = (focused_index + 1) % len(windows)  # Wrap around to the start if at the end
            windows[next_index][0].minimize()
            windows[next_index][0].restore()
            print("focused " + str(windows[next_index][0].title))

def focus_previous_window():
    ctypes.windll.user32.AllowSetForegroundWindow(ctypes.windll.kernel32.GetCurrentProcessId())
    windows = getwindows()
    if len(windows) >= 2:
        focused_index = next((i for i, (w, f) in enumerate(windows) if f == 1), None)
        windows = getwindows()
        if focused_index is not None and focused_index > 0:
            previous_index = (focused_index - 1) % len(windows)  # Wrap around to the end if at the start
            windows[previous_index][0].minimize()
            windows[previous_index][0].restore()
            print("focused " + str(windows[previous_index][0].title))

def getwindows():
    # Get monitor dimensions
    height = screeninfo.get_monitors()[0].height - 40
    width = screeninfo.get_monitors()[0].width

    # Get all windows that are not minimized or maximized and have a title
    all_windows = [
        window for window in gw.getAllWindows()
        if window.title != '' and not (window.isMinimized or window.isMaximized)
        and window.title != 'Program Manager' and window.title != 'Microsoft Text Input Application'
    ]

    # Filter windows based on size
    filtered_windows = [
        window for window in all_windows
        if window.height < height or window.width < width
    ]

    # Filter out windows that are completely covered by other windows
    visible_windows = [
        window for window in filtered_windows
        if not is_fully_covered(window, filtered_windows)
    ]

    # Sort windows from left to right based on their positions
    sorted_windows = sorted(visible_windows, key=lambda w: w.left)

    # Create tuples with window and its focus state (1 if focused, 0 if not)
    windows_with_focus_state = [
        (window, 1 if window.isActive else 0) for window in sorted_windows
    ]
    return windows_with_focus_state