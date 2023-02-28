import pwinput
import base64
import os


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


username = input("Username: ")
original = pwinput.pwinput(prompt="Password: ", mask="•")
obfuscated = obfuscate(original)
fh = open('creds.txt', 'w')
fh.write(f"{username}\n")
fh.write(f"{obfuscated}")
fh.close()

creds = open('creds.txt', 'r')
creds.seek(0)
lines = creds.readlines()
username = lines[0].strip()
password = lines[1].strip()
password = deobfuscate(password)
print(f"USERNAME={username}\nPASSWORD={password}")
creds.close()

input("Press enter to delete the password:")
if os.path.exists("creds.txt"):
  os.remove("creds.txt")
else:
  print("The file does not exist")

if os.path.exists("creds.txt"):
    creds = open('creds.txt', 'r')
    creds.seek(0)
    lines = creds.readlines()
    username = lines[0].strip()
    password = lines[1].strip()
    password = deobfuscate(password)
    print(f"USERNAME={username}\nPASSWORD={password}")
else:
    print("No credentials saved.")



