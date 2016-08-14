import win32gui

def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        print win32gui.GetWindowText(hwnd),hwnd
        if 'Skillsoft' in win32gui.GetWindowText(hwnd) or 'mmlviewer' in win32gui.GetWindowText(hwnd) or 'CSDialog' in win32gui.GetWindowText(hwnd):
            #win32gui.MoveWindow(hwnd, 0, 0, 760, 500, True)
            win32gui.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0001)


win32gui.EnumWindows(enumHandler, None)
