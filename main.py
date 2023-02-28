from msvcrt import getch
import paramiko
import time
import sys
import colorama
import getpass
import keyboard

colorama.init()


def shell(chan):
    global decoder, dn
    decoder = ""
    import threading

    def writeall(sock):
        global dn
        dn = ""
        while True:
            data = sock.recv(256)
            decoder = str(data.decode("utf8", "ignore"))
            if not data:
                sys.stdout.write("\r\n\n*** DISCONNECTED ***\r\n\r\n")
                sys.stdout.flush()
                remote_conn.close()
                sys.exit()
            sys.stdout.write(decoder)
            if decoder.endswith(": ") or decoder.endswith("# ") or decoder.endswith("> "):
                dl = decoder.splitlines()
                dn = len(dl[-1])
            sys.stdout.flush()
            if "Type the hot key to suspend the connection: <CTRL>Z" in decoder:
                sys.stdout.write(f"\r\033[1F\033[2KType the hot key to suspend the connection: <CTRL>C\n")
            # if "--More--" in decoder:
            #     time.sleep(.1)
            #     chan.send("  ")

    writer = threading.Thread(target=writeall, args=(chan,))
    writer.start()

    try:
        while True:
            if dn != "":
                sys.stdout.write("\033[1A" + "\033[C" * int(dn))
            try:
                d = sys.stdin.readline()
            except EOFError:
                print(EOFError)
                break
            except KeyboardInterrupt:
                d = chr(3)
            if not d:
                break
            elif d == "set_phone_home\n":
                chan.send("exec batch start\n")
                time.sleep(.5)
                chan.send("config system central-management\n")
                time.sleep(.5)
                chan.send("set type fortimanager\n")
                time.sleep(.5)
                chan.send("set serial-number \"FMG-VM0A16000497\"\n")
                time.sleep(.5)
                chan.send("set fmg \"172.85.135.226\"\n")
                time.sleep(.5)
                chan.send("end\n")
                time.sleep(.5)
                chan.send("exec batch end\n")
            elif d == "firmware_up\n":
                chan.send("\rexecute restore image usb image.out\n")
                sys.stdout.write("\033[F")
                time.sleep(.5)
                chan.send("y")
            elif d == "quit_ssh\n":
                remote_conn.close()
                sys.exit()
            else:
                chan.send(d)





    except EOFError:
        # user hit ^Z or F6
        # remote_conn.close()
        print(EOFError)
        pass
    except KeyboardInterrupt:
        chan.send(chr(3))
        remote_conn.close()
        time.sleep(3)
        sys.exit()


def get_serv():
    global serv
    serv = input("COM: ")
    try:
        serv = int(serv)
    except:
        get_serv()


def get_portx():
    global portx
    portx = input("Port: ")
    try:
        portx = int(portx)
    except:
        get_portx()


print("\n(╯°□°)╯_- \u001b[31m♥\033[39m FortiSSH Client \u001b[31m♥\033[39m\n")

serv = 0
portx = 0
serv_list = [17, 18, 19, 200]
while serv not in serv_list:
    get_serv()
while not 0 < portx < 49:
    get_portx()

if serv == 17:
    ip = '192.168.40.17'
    username = 'mmarcotte'
    password = 'Beretta0423!'
    port = "30" + f"{portx:02}"
elif serv == 18:
    ip = '192.168.40.18'
    username = input("User name: ")
    password = input("Password: ")
    port = "30" + f"{portx:02}"
elif serv == 19:
    ip = '192.168.40.19'
    username = 'mmarcotte'
    password = 'Mikey04231!'
    port = "22" + f"{portx:02}"
elif serv == 200:
    ip = '192.168.41.200'
    username = 'mmarcotte'
    password = 'Mikey04231!'
    port = "30" + f"{portx:02}"

# username = input("User name: ")
# password = pwinput.pwinput(prompt="Password: ", mask="•")


# port = 3001

# Create instance of SSHClient object
remote_conn_pre = paramiko.SSHClient()

# Automatically add untrusted hosts (make sure okay for security policy in your environment)
remote_conn_pre.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())

# initiate SSH connection
remote_conn_pre.connect(ip, username=username, password=password, port=port, look_for_keys=False, allow_agent=False)

print(f"\nSSH connection established to {ip}, Port {portx}")

# Use invoke_shell to establish an 'interactive session'
remote_conn = remote_conn_pre.invoke_shell()
shell(remote_conn)
remote_conn.close()
