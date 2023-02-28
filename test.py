from msvcrt import getch
import sys

# while True:
#     keycode = ord(getch())
#     if keycode == 27:  # ESC
#         break
#     elif keycode == 13:  # Enter
#         print(keycode)
#     elif keycode == 224:  # Special keys (arrows, f keys, ins, del, etc.)
#         keycode = ord(getch())
#         if keycode == 80:  # Down arrow
#             print("down")
#         elif keycode == 72:  # Up arrow
#             print("up")
#     elif keycode == 3:
#         sys.exit()



d = ""
while True:
    key = getch()
    print(key)
    if key != b'\x03':
        if key == b'\xe0':
            keycode = ord(getch())
            if keycode == 80:  # Down arrow
                print("down")
            elif keycode == 72:  # Up arrow
                print("up")
        if key == b'\x08':
            if d == "":
                pass
            else:
                d = d.rstrip(d[-1])
                sys.stdout.write('\b \b')
        else:
            # key = key.decode('utf-8')
            print(key)
            # d = d + key
        if key == "\r":
            d = ""
            sys.stdout.write('\n')
    else:
        sys.exit()
    sys.stdout.flush()

"""
ctrl + c: b'\x03'
ctrl + z: b'\x1a'
backspace: b'\x08'
space: b' '
up: b'\xe0' + b'H'
"""
