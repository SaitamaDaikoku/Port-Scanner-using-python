#  Python Port Scanner

A simple multi-threaded TCP port scanner built using Python.
This project uses socket programming and concurrent execution to scan open ports on a target system efficiently.

---

##  Features

* Multi-threaded port scanning
* Custom port range support
* IP address and domain scanning
* Lightweight and fast
* Command-line interface

---

##  Technologies Used

* Python 3
* Socket Programming
* ThreadPoolExecutor
* argparse

---

##  Usage

Run the scanner:

```bash id="b9mq4n"
python port_scanner.py <target>
```

Example:

```bash id="n7g2d3"
python port_scanner.py scanme.nmap.org
```

Scan a custom port range:

```bash id="u8a1px"
python port_scanner.py scanme.nmap.org --start 20 --end 100
```

Increase thread count:

```bash id="iy8h8n"
python port_scanner.py 127.0.0.1 --start 1 --end 1000 --threads 200
```

---

##  Project Structure

```text id="f5jccz"
port-scanner/
│
├── port_scanner.py
├── README.md
└── requirements.txt
```

---

##  Concepts Used

* TCP socket connections
* Multithreading
* Concurrent execution
* Network communication
* CLI argument parsing

---

##  Example Output

```text id="ph8klz"
Scanning scanme.nmap.org from port 1 to 100...

[OPEN] Port 22
[OPEN] Port 80
```

---

##  Disclaimer

This project is intended for educational purposes only.
Only scan systems you own or have permission to test.

---

##  Author
Sanjiv R Btech CSE Student
