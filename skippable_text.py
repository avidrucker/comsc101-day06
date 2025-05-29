# unique from the simple typewriter.py program,
# this program allows the user to press the Enter
# key and "skip" to the finished fully printed
# out text without any time delay

import time
import threading
import sys

skip_delay = False
chars_printed = 0

def wait_for_enter():
    global skip_delay

    try:
        # Windows
        import msvcrt
        while True:
            if msvcrt.kbhit():
                if msvcrt.getch() == b'\r':  # Enter key
                    skip_delay = True
                    break
    except ImportError:
        # Unix (Linux, macOS)
        import sys
        import termios
        import tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)
            while True:
                ch = sys.stdin.read(1)
                if ch == '\n':  # Enter key
                    skip_delay = True
                    break
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

# Start thread to listen for Enter key without echoing newline
threading.Thread(target=wait_for_enter, daemon=True).start()

some_string = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

for char in some_string:
    print(char, end='', flush=True)
    if not skip_delay:
        time.sleep(0.05)
    chars_printed += 1
