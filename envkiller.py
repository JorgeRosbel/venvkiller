#!/usr/bin/env python3

import os 
import shutil
import curses
import colorama



def red_text(text):
    return colorama.Fore.RED + text + colorama.Style.RESET_ALL

def green_text(text):
    return colorama.Fore.GREEN + text + colorama.Style.RESET_ALL

def yellow_text(text):
    return colorama.Fore.YELLOW + text + colorama.Style.RESET_ALL


def get_size(size):
    kb = 1024
    mb = kb * 1024
    gb = mb * 1024

    
    if size < kb:
        return f"{size} B", size
    elif size < mb:
        return f"{size / kb} KB", size
    elif size < gb:
        return f"{size / mb} MB", size
    else:
        return f"{size / gb} GB", size


def get_venv():
    venv_list = []

    for root, dirs, files in os.walk("."):
        for dir in dirs:
            if dir == ".venv" or dir == "venv" or dir == "env":
                path = os.path.join(root, dir)
                abs_path = os.path.realpath(path)
                venv_list.append({"path": abs_path, "status": "AVAILABLE", "size": get_size(os.path.getsize(abs_path))})
    return venv_list
               


def menu(stdscr, venv_list):
    curses.curs_set(0)  # Hide cursor
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)

    current_row = 0
    
    while True:
        stdscr.clear()
        
        # Calculate totals
        total_size = sum(v['size'][1] for v in venv_list)
        saved_size = sum(v['size'][1] for v in venv_list if v['status'] == 'DELETED')

        # Header
        stdscr.addstr(0, 0, "--- Virtual Environments ---", curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(1, 0, f"Total size: {get_size(total_size)[0]}")
        stdscr.addstr(2, 0, f"Total saved: {get_size(saved_size)[0]}")
        stdscr.addstr(3, 0, "Select env to delete (SPACE/ENTER), navigate (ARROWS), Quit (q):")

        # List
        max_y, max_x = stdscr.getmaxyx()
        
        for i, folder in enumerate(venv_list):
            y = 5 + i
            if y >= max_y - 1: # Avoid writing to last line or off screen
                break
                
            if i == current_row:
                stdscr.attron(curses.A_REVERSE)

            status_color = curses.color_pair(2) if folder['status'] == 'AVAILABLE' else curses.color_pair(1)
            path_color = curses.color_pair(3)
            size_color = curses.color_pair(2)
            
            # Construct line parts
            prefix = f"{i}. ["
            status_text = folder['status']
            suffix = "] - "
            path_text = folder['path']
            size_text = f" - {folder['size'][0]}"
            
            try:
                # Print Prefix
                stdscr.addstr(y, 0, prefix)
                
                # Print Status with Color
                stdscr.addstr(status_text, status_color)
                
                # Print Suffix
                stdscr.addstr(suffix)
                
                # Calculate space for path
                cur_y, cur_x = stdscr.getyx()
                remaining = max_x - cur_x - len(size_text) - 1
                
                if remaining > 3:
                    print_path = path_text
                    if len(print_path) > remaining:
                        print_path = print_path[:remaining-3] + "..."
                    stdscr.addstr(print_path, path_color)
                
                # Print Size
                stdscr.addstr(size_text, size_color)
                
            except curses.error:
                pass 

            if i == current_row:
                stdscr.attroff(curses.A_REVERSE)

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(venv_list) - 1:
            current_row += 1
        elif key == ord(' ') or key == 10: 
            if venv_list[current_row]['status'] == 'AVAILABLE':
                venv_list[current_row]['status'] = 'DELETED'
                shutil.rmtree(venv_list[current_row]['path'])

        elif key == ord('q'):
            break

out = get_venv()

if out:
    curses.wrapper(menu, out)
else:
    print("No environments found.")






