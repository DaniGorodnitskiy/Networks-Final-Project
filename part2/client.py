import socket
import threading

HOST = '127.0.0.1'
PORT = 9999

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode('utf-8')
            if not msg: break
            print(f"\n{msg}\n>> ", end="")
        except:
            print("Disconnected.")
            sock.close()
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
    except:
        print("Server not found.")
        return

    username = input("Username: ")
    client.send(username.encode('utf-8'))

    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    print("Connected! To chat type: 'Target: Message'")
    while True:
        msg = input(">> ")
        if msg == 'quit': break
        client.send(msg.encode('utf-8'))
    client.close()

if __name__ == "__main__":
    start_client()