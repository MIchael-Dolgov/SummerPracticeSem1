from menu_manager import menu, display_menu
from constants import MENU_FILE
from filelib import buffer_enable

def app():
    buffer_enable()
    working = True
    while working:
        display_menu(MENU_FILE, "s", "\033[0;32m")
        display_menu(MENU_FILE, "m")
        display_menu(MENU_FILE, "?", color="\033[;1m"+ "\033[93m", endd="")
        request = input()
        working = menu(request)


if(__name__=="__main__"):
    app()
else:
    raise "Это не модуль!"
