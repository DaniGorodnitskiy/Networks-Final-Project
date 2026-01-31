# Computer Networks Final Project - TCP Chat & Traffic Analysis

This repository contains the final project for the Computer Networks course. The project is divided into two main parts:
1. **Packet Encapsulation:** Manual creation of TCP/IP packets using Scapy based on CSV input.
2. **Chat Application:** A multi-threaded TCP Client-Server chat room implementation in Python.

---

## 📂 Project Structure

**Part 1: Traffic Simulation**
- `web_server.ipynb`: Jupyter Notebook that reads the CSV and generates TCP packets using Scapy.
- `group209186378_http_input.csv`: The input file containing the application layer messages.
- `capture.pcapng`: Wireshark capture of the generated traffic.

**Part 2: Chat Application**
- `server.py`: The TCP server handling multiple clients using threading.
- `client.py`: The TCP client for sending/receiving messages.
- `protocol_definition.txt`: Documentation of the application layer protocol and memory structure.
- `chat_capture.pcapng`: Wireshark capture of a chat session.
- `user_guide.txt`: Detailed execution instructions.

---

## 🚀 Part 1: Packet Encapsulation (Scapy)

### How to Run:
1. Open `web_server.ipynb` in Jupyter Notebook or VS Code.
2. Ensure you have the `scapy` library installed.
3. Run all cells in the notebook.
4. The script will read `group209186378_http_input.csv` and send the packets over the loopback interface (127.0.0.1).

---

## 💬 Part 2: Chat Application

A fully functional chat system allowing multiple users to communicate via a central server.

### Features:
- **TCP Sockets:** Pure socket implementation (no high-level frameworks).
- **Multi-Threading:** Handles multiple clients simultaneously without blocking.
- **Direct Messaging:** Routes messages to specific users.

### How to Run:

### 1. Start the Server
Open a terminal (CMD) in the project folder and run:

    python server.py

You should see:

    [*] Server listening on 127.0.0.1:9999

### 2. Start Clients (Open multiple terminals)
**Important:** Do not close the server window!
To simulate a conversation, you need to open **new** terminal windows for the clients.

**Step A: Connect First User (Chechik)**
1. Open a new terminal window.
2. Run the client script:

       python client.py

3. When prompted, enter a username (e.g., Chechik).
4. You should see: `Connected to server`.

**Step B: Connect Second User (Nerli)**
1. Open **another** new terminal window.
2. Run the client script again:

       python client.py

3. Enter a different username (e.g., Nerli).

### 3. Usage
To send a message, use the format: `RecipientName: Message`

**Example (Chechik sending to Nerli):**

    Nerli: Hello Nerli, did you get my packet?

---

## 🛠 Prerequisites
- Python 3.x
- Libraries: `socket`, `threading`, `pandas`, `scapy`
- Wireshark (for viewing .pcap files)

## 📝 Authors
Daniel Gorodnitskiy 209186378
