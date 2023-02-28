import base64
import colorama
import logging
import os
import paramiko
import pwinput
import sys
import threading
import time
from msvcrt import getch, kbhit
from pynput.keyboard import Controller

os.system("title " + "FortiSSH Client")
colorama.init()
d = ""
keyboard = Controller()


def get_serv():
    global serv
    serv = input("COM: ")
    try:
        serv = int(serv)
    except:
        sys.stdout.write("\033[A" + "\033[K" + " " * 40 + "\033[D" * 40)
        get_serv()


def get_portx():
    global portx
    portx = input("Port: ")
    try:
        portx = int(portx)
    except:
        sys.stdout.write("\033[A" + "\033[K" + " " * 40 + "\033[D" * 40)
        get_portx()


def ssh_login():
    global remote_conn_pre, ip, portx

    def obfuscate(plainText):
        plainBytes = plainText.encode('ascii')
        encodedBytes = base64.b64encode(plainBytes)
        encodedText = encodedBytes.decode('ascii')
        return encodedText

    def deobfuscate(obfuscatedText):
        obfuscatedBytes = obfuscatedText.encode('ascii')
        decodedBytes = base64.b64decode(obfuscatedBytes)
        decodedText = decodedBytes.decode('ascii')
        return decodedText

    def encrypt(pw):
        encrypted = obfuscate(obfuscate(obfuscate(pw)))
        return encrypted

    def decrypt(pw):
        decrypted = deobfuscate(deobfuscate(deobfuscate(pw)))
        return decrypted

    remote_conn_pre = paramiko.SSHClient()
    logging.getLogger("paramiko").setLevel(logging.ERROR)

    remote_conn_pre.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())

    if serv == 17:
        ip = '192.168.40.17'
        port = "30" + f"{portx:02}"
        if os.path.exists("creds17.txt"):
            creds = open('creds17.txt', 'r')
            creds.seek(0)
            lines = creds.readlines()
            username17 = lines[0].strip()
            password17 = lines[1].strip()
            try:
                password17 = decrypt(password17)
                creds.close()
            except:
                creds.close()
                pass
        else:
            username17 = input("User name: ")
            password17 = pwinput.pwinput(prompt="Password: ", mask="•")

        try:
            try:
                remote_conn_pre.connect(ip, username=username17 + ":" + port, password=password17, port=22, look_for_keys=False,
                                        allow_agent=False)
                if not os.path.exists("creds17.txt"):
                    save_creds = input("Do you want to save your credentials? (y/n): ")
                    if save_creds == "y":
                        obfuscated17 = encrypt(password17)
                        fh = open('creds17.txt', 'w')
                        fh.write(f"{username17}\n")
                        fh.write(f"{obfuscated17}")
                        fh.close()
            except:
                if os.path.exists("creds17.txt"):
                    print(f"\nDeleting invalid stored credentials, please try again.\n")
                    os.remove("creds17.txt")
                else:
                    print(
                        f"\nInvalid credentials, please try again.\n\nFirst time logging in? Update your password at "
                        f"[https://{ip}]\n")
                ssh_login()
        except:
            time.sleep(3)
            sys.exit()
    elif serv == 18:
        ip = '192.168.40.18'
        port = "30" + f"{portx:02}"
        if os.path.exists("creds18.txt"):
            creds = open('creds18.txt', 'r')
            creds.seek(0)
            lines = creds.readlines()
            username18 = lines[0].strip()
            password18 = lines[1].strip()
            try:
                password18 = decrypt(password18)
                creds.close()
            except:
                creds.close()
                pass
        else:
            username18 = input("User name: ")
            password18 = pwinput.pwinput(prompt="Password: ", mask="•")

        try:
            try:
                remote_conn_pre.connect(ip, username=username18 + ":" + port, password=password18, port=22, look_for_keys=False,
                                        allow_agent=False)
                if not os.path.exists("creds18.txt"):
                    save_creds = input("Do you want to save your credentials? (y/n): ")
                    if save_creds == "y":
                        obfuscated18 = encrypt(password18)
                        fh = open('creds18.txt', 'w')
                        fh.write(f"{username18}\n")
                        fh.write(f"{obfuscated18}")
                        fh.close()
            except:
                if os.path.exists("creds18.txt"):
                    print(f"Deleting invalid stored credentials, please try again.\n")
                    os.remove("creds18.txt")
                else:
                    print(
                        f"Invalid credentials, please try again.\n\nFirst time logging in? Update your password at ["
                        f"https://{ip}]\n")
                ssh_login()
        except:
            time.sleep(3)
            sys.exit()
    elif serv == 19:
        ip = '192.168.40.19'
        port = "22" + f"{portx:02}"
        if os.path.exists("creds19.txt"):
            creds = open('creds19.txt', 'r')
            creds.seek(0)
            lines = creds.readlines()
            username19 = lines[0].strip()
            password19 = lines[1].strip()
            try:
                password19 = decrypt(password19)
                creds.close()
            except:
                creds.close()
                pass
        else:
            username19 = input("User name: ")
            password19 = pwinput.pwinput(prompt="Password: ", mask="•")

        try:
            try:
                remote_conn_pre.connect(ip, username=username19 + ":" + port, password=password19, port=22, look_for_keys=False,
                                        allow_agent=False)
                if not os.path.exists("creds19.txt"):
                    save_creds = input("Do you want to save your credentials? (y/n): ")
                    if save_creds == "y":
                        obfuscated19 = encrypt(password19)
                        fh = open('creds19.txt', 'w')
                        fh.write(f"{username19}\n")
                        fh.write(f"{obfuscated19}")
                        fh.close()
            except:
                if os.path.exists("creds19.txt"):
                    print(f"Deleting invalid stored credentials, please try again.\n")
                    os.remove("creds19.txt")
                else:
                    print(
                        f"Invalid credentials, please try again.\n\nFirst time logging in? Update your password at ["
                        f"https://{ip}]\n")
                ssh_login()
        except:
            time.sleep(3)
            sys.exit()
    elif serv == 200:
        ip = '192.168.41.200'
        port = "30" + f"{portx:02}"
        # username200 = 'mmarcotte'
        # password200 = 'Mikey04231!'
        if os.path.exists("creds200.txt"):
            creds = open('creds200.txt', 'r')
            creds.seek(0)
            lines = creds.readlines()
            username200 = lines[0].strip()
            password200 = lines[1].strip()
            try:
                password200 = decrypt(password200)
                creds.close()
            except:
                creds.close()
                print(f"Deleting invalid stored credentials, please try again.\n")
                os.remove("creds200.txt")
        else:
            username200 = input("User name: ")
            password200 = pwinput.pwinput(prompt="Password: ", mask="•")

        try:
            try:
                remote_conn_pre.connect(ip, username=username200 + ":" + port, password=password200, port=22, look_for_keys=False,
                                        allow_agent=False)
                if not os.path.exists("creds200.txt"):
                    save_creds = input("Do you want to save your credentials? (y/n): ")
                    if save_creds == "y":
                        obfuscated200 = encrypt(password200)
                        fh = open('creds200.txt', 'w')
                        fh.write(f"{username200}\n")
                        fh.write(f"{obfuscated200}")
                        fh.close()
            except Exception as e:
                print(e)
                if os.path.exists("creds200.txt"):
                    print(f"Deleting invalid stored credentials, please try again.\n")
                    os.remove("creds200.txt")
                else:
                    print(
                        f"Invalid credentials, please try again.\n\nFirst time logging in? Update your password at ["
                        f"https://{ip}]\n")
                ssh_login()
        except:
            time.sleep(3)
            sys.exit()


def shell(chan):
    global decoder, dn, d
    decoder = ""

    def writeall(sock):
        global dn, d, dl
        dn = ""
        dl = ""
        while True:
            data = sock.recv(256)
            decoder = str(data.decode("utf8", "ignore"))
            if not data:
                sys.stdout.write("\r\n\n*** DISCONNECTED ***\r\n\r\n")
                break
            sys.stdout.write(decoder)
            sys.stdout.flush()
            dl = decoder.splitlines()
            if len(dl[-1]) > 5:
                #     if dl[-1].endswith(("# ", "#", "> ", ">", ": ", ":", ")", ") ")):
                dn = len(dl[-1])
            if "Type the hot key to suspend the connection: <CTRL>Z" in decoder:
                sys.stdout.write(f"\r\033[1F\033[2KType <CTRL>K to view quick commands or <CTRL>Z to end the session.\n")
                time.sleep(.2)
                chan.send("\r")

    writer = threading.Thread(target=writeall, args=(chan,))
    writer.daemon = True
    writer.start()

    try:
        if dn != "":
            sys.stdout.write("\033[C" * int(dn) + " " * 40 + "\033[D" * 40)
            sys.stdout.flush()
        while True:
            key = getch()
            if key != b'\x1a':
                if key == b'\x0b':
                    sys.stdout.write(f"""
clscr             clear screen
enter_config      automatically enter saved config file (.txt only)
firmware_up       upgrade firmware from USB
set_phone_home    run phone-home batch script
quit_ssh          quick exit
usb_bak           export config to USB

{dl[-1]}""")
                elif key == b'\x08':
                    if d == "":
                        chan.send("\b")
                    else:
                        d = d.rstrip(d[-1])
                        sys.stdout.write('\b \b')
                        sys.stdout.flush()
                elif key == b' ':
                    if d == "":
                        # sys.stdout.write(" ")
                        chan.send(" ")
                        d = ""
                    else:
                        if not d.endswith(" "):
                            sys.stdout.write(" ")
                            sys.stdin.flush()
                        d = d + " "
                elif key == b'\x03':
                    d == ""
                    chan.send(chr(3))
                elif key == b'\xe0':
                    keycode = ord(getch())
                    if keycode == 80:  # Down arrow
                        d == ""
                        chan.send("\u001b[B")
                    elif keycode == 72:  # Up arrow
                        d == ""
                        chan.send("\u001b[A")
                elif key == b'?':
                    if d != "":
                        sys.stdout.write("?\n")
                    else:
                        sys.stdout.write("?")
                    sys.stdout.flush()
                    chan.send(d + "?")
                    # sys.stdout.write("\033[C" * len(d) + " " * 40 + "\033[D" * 40)
                    d = ""
                else:
                    key = key.decode('utf-8')
                    d = d + key
                    sys.stdout.write(key)
                    sys.stdout.flush()
                if key == "\r" or key == "\n":
                    if not d:
                        break
                    elif d.lstrip() == "usb_bak\r":
                        bak_file = input("\nFilename: ")
                        bak_file = ''.join(e for e in bak_file if e.isalnum() or e == ("-" or "_"))
                        chan.send(f"exec backup full-config usb {bak_file}\r")
                        d = ""
                    elif d.lstrip() == "enter_config\r":
                        filename = input("\nEnter the filename: ")
                        sys.stdout.write(dl[-1])
                        try:
                            if filename.endswith(".txt"):
                                config_file = open(f'{filename}', 'r')
                            else:
                                config_file = open(f'{filename}.txt', 'r')
                            for line in config_file:
                                chan.send(line)
                                time.sleep(.1)
                            chan.send("\r")
                        except Exception as e:
                            print(e)
                            chan.send("\r")
                        d = ""
                    elif d.lstrip() == "set_phone_home\r":
                        sys.stdout.write("\033[C" * int(dn) + " " * 40 + "\033[D" * 40)
                        chan.send("exec batch start\r")
                        time.sleep(.5)
                        chan.send("config system central-management\r")
                        time.sleep(.5)
                        chan.send("set type fortimanager\r")
                        time.sleep(.5)
                        chan.send("set serial-number \"FMG-VM0A16000497\"\r")
                        time.sleep(.5)
                        chan.send("set fmg \"172.85.135.226\"\r")
                        time.sleep(.5)
                        chan.send("end\r")
                        time.sleep(.5)
                        sys.stdout.write("\033[D" * int(dn))
                        chan.send("exec batch end\r")
                        d = ""
                    elif d.lstrip() == "firmware_up\r":
                        sys.stdout.write("\033[C" * int(dn) + " " * 40 + "\033[D" * 40)
                        chan.send("\rexecute restore image usb image.out\r")
                        sys.stdout.write("\033[F")
                        time.sleep(.5)
                        chan.send("y")
                        time.sleep(.2)
                        sys.stdout.write("\033[D" * int(dn))
                        d = ""
                    elif d.lstrip() == "quit_ssh\r":
                        print("\n\nGoodbye!")
                        time.sleep(1)
                        sys.exit()
                    elif d == "y\r" and dl[-1].endswith(("(y/n)", "(y/n) ")):
                        chan.send("y")
                        d = ""
                    elif d == "n\r" and dl[-1].endswith(("(y/n)", "(y/n) ")):
                        chan.send("n")
                        d = ""
                    elif d.lstrip() == "clscr\r":
                        os.system('cls')
                        print("\n(╯°□°)╯_- \u001b[31m♥\033[39m FortiSSH Client \u001b[31m♥\033[39m\n")
                        sys.stdout.write("\033[K" + dl[-1] + "\033[D" * int(dn))
                        sys.stdout.flush()
                        d = ""
                    elif d.strip().endswith("?"):
                        chan.send(d.strip())
                        d = ""
                    else:
                        if not dl:
                            chan.send(d.strip() + "\r")
                        elif "more--" in dl[-1].lower():
                            chan.send(" \b")
                        else:
                            chan.send(d.strip() + "\r")
                        d = ""
                    if dn != "":
                        sys.stdout.write("\033[C" * int(dn) + " " * 40 + "\033[D" * 40)
                        sys.stdout.flush()

                    sys.stdout.flush()
            else:
                chan.send(chr(3))
                break
            sys.stdout.flush()
    except EOFError:
        print(EOFError)
        chan.send(chr(3))
    except KeyboardInterrupt:
        d = chr(3)


def main_loop():
    global serv, portx, port
    os.system('cls')
    print("\n(╯°□°)╯_- \u001b[31m♥\033[39m FortiSSH Client \u001b[31m♥\033[39m\n\n")

    serv = 0
    portx = 0
    serv_list = [17, 18, 19, 200]
    try:
        while serv not in serv_list:
            sys.stdout.write("\033[A" + "\033[K" + " " * 40 + "\033[D" * 40)
            get_serv()
    except:
        sys.exit()
    try:
        while not 0 < portx < 49:
            sys.stdout.write("\033[A" + "\033[K" + " " * 40 + "\033[D" * 40)
            get_portx()
    except:
        sys.exit()
    sys.stdout.write("\033[A" + "\033[K" + " " * 40 + "\033[D" * 40)
    ssh_login()

    print(f"SSH connection established to {ip}, Port {portx}")
    # print("Type the hot key to show quick commands: <CTRL>K")
    # time.sleep(.2)
    remote_conn = remote_conn_pre.invoke_shell()
    shell(remote_conn)
    remote_conn.close()
    sys.stdout.write("Press any key within the next 3 seconds to start a new session.")
    sys.stdout.flush()
    startTime = time.time()
    while True:
        if kbhit():
            getch()
            main_loop()
        elif time.time() - startTime > 3:
            break
        time.sleep(.1)

try:
    main_loop()
    sys.exit()
except:
    print("\n\nGoodbye!")
    time.sleep(1)
    sys.exit()
print("\n\nGoodbye!")
time.sleep(1)
sys.exit()
