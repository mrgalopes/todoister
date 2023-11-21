import subprocess


def notify(title, message):
    subprocess.run(["notify-send", f"{title}", f"{message}", "-a", "Todoister"])
