import time

from simple_term_menu import TerminalMenu
from request_weather import Weather

class Menu():

    def main():
        main_menu_title = "  Main Menuxd\n"
        main_menu_items = ["Edit Menu", "Show Weather", "Pogoda dla Gdańsk", "Quit"]
        main_menu_cursor = "> "
        main_menu_cursor_style = ("fg_red", "bold")
        main_menu_style = ("bg_red", "fg_yellow")
        main_menu_exit = False

        weather = Weather()

        main_menu = TerminalMenu(
            menu_entries=main_menu_items,
            title=main_menu_title,
            menu_cursor=main_menu_cursor,
            menu_cursor_style=main_menu_cursor_style,
            menu_highlight_style=main_menu_style,
            cycle_cursor=True,
            clear_screen=True,
        )

        edit_menu_title = "  Edit Menu\n"
        edit_menu_items = ["Edit Config", "Save Settings", "Back to Main Menu"]
        edit_menu_back = False
        edit_menu = TerminalMenu(
            edit_menu_items,
            title=edit_menu_title,
            menu_cursor=main_menu_cursor,
            menu_cursor_style=main_menu_cursor_style,
            menu_highlight_style=main_menu_style,
            cycle_cursor=True,
            clear_screen=True,
        )

        while not main_menu_exit:
            main_sel = main_menu.show()

            if main_sel == 0:
                while not edit_menu_back:
                    edit_sel = edit_menu.show()
                    if edit_sel == 0:
                        print("Edit Config Selected")
                        time.sleep(5)
                    elif edit_sel == 1:
                        print("Save Selected")
                        time.sleep(5)
                    elif edit_sel == 2:
                        edit_menu_back = True
                        print("Back Selected")
                edit_menu_back = False
            elif main_sel == 1:
                print("Show Weather selected")
                weather.show_weather()
                time.sleep(5)
            elif main_sel == 2:
                print("option 3 selected")
                weather.show_weather_default()
                time.sleep(5)
            elif main_sel == 3:
                main_menu_exit = True
                print("Quit Selected")


       

