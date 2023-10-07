import keyboard

recorded_keys = keyboard.record('a')
string_ver = keyboard.get_typed_strings(recorded_keys)
f = open("./out.txt", "w")
for i in string_ver:
    f.write(i)
f.close()