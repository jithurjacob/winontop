import sys
import win32gui
 
def enumHandler(hwnd, lParam):
    """The windows on top functionality is taken here
    Source: http://stackoverflow.com/questions/1482565/how-to-make-python-window-run-as-always-on-top"""
    if win32gui.IsWindowVisible(hwnd):
        if sys.argv[1].lower() in win32gui.GetWindowText(hwnd).lower():
            win32gui.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0001)
            return True


def showDoc():
    print(
        """Help Documentation
Hey folks this is an easy to use tool to keep windows on top of others.
You have to specify only a part of the name in windows name. No need to install any third party software.
If you want a chrome tab to be on top just mention any word in the title.

For eg. if you want youtube video "Game of Thrones Season 6: Episode #9 Preview (HBO)" on top
>>> winontop thrones
or
>>> winontop games

For help doc
>>> winontop -h

Tested on Windows 10/Python2
Feel free to contribute or report any issues at https://github.com/jithurjacob/winontop"""
        )

def main():
    """
    Argument Parsing and help documentation
    """
    if len(sys.argv) != 2:
        print("Incorrect number of arguments. Use -h for help")
    else:
        if sys.argv[1] in ["-h", "--h", "-help"]:
            showDoc()
        else:
            win32gui.EnumWindows(enumHandler, None)

if __name__ == '__main__':
    main()
