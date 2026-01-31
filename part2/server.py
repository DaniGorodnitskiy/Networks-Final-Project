import socket
import threading

# הגדרות חיבור
HOST = '127.0.0.1'
PORT = 9999

clients = {}

def handle_client(client_socket):
    username = ""
    try:
        # קבלת שם המשתמש
        username = client_socket.recv(1024).decode('utf-8')
        clients[username] = client_socket
        print(f"[+] User '{username}' connected.")
        client_socket.send(f"Welcome {username}!".encode('utf-8'))

        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            
            print(f"[{username}]: {message}")
            
            # לוגיקת ניתוב הודעות (שם: הודעה)
            if ":" in message:
                target_name, msg_content = message.split(":", 1)
                target_name = target_name.strip()
                
                if target_name in clients:
                    clients[target_name].send(f"{username}: {msg_content}".encode('utf-8'))
                else:
                    client_socket.send(f"User {target_name} not found.".encode('utf-8'))
            else:
                client_socket.send("Format error. Use 'Target: Message'".encode('utf-8'))

    except:
        pass
    finally:
        if username in clients:
            del clients[username]
            client_socket.close()
            print(f"[-] User '{username}' disconnected.")  # הוספנו את השורה הזו

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[*] Server listening on {HOST}:{PORT}")

    while True:
        client_sock, addr = server.accept()
        threading.Thread(target=handle_client, args=(client_sock,)).start()

if __name__ == "__main__":
    start_server()