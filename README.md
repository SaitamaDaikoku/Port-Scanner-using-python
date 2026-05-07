# Python Multi-Threaded Port Scanner

A high-performance multi-threaded TCP port scanner developed in Python using socket programming and concurrent execution techniques.
This project demonstrates core software engineering concepts such as network communication, concurrency, CLI development, and scalable task execution.

---

## Overview

The Port Scanner is a command-line networking utility that scans a target host for open TCP ports within a specified range.
It uses Python’s `socket` module for low-level network communication and `ThreadPoolExecutor` for concurrent scanning to improve performance and efficiency.

This project was built to strengthen practical understanding of:

* Networking fundamentals
* Concurrent programming
* System-level utilities
* Python backend development concepts
* Performance optimization techniques

---

## Features

* Multi-threaded TCP port scanning
* Customizable port range
* Domain name and IP address support
* Configurable thread pool size
* Lightweight and dependency-free
* Clean CLI-based architecture
* Optimized scanning using concurrency

---

## Tech Stack

| Technology         | Purpose                   |
| ------------------ | ------------------------- |
| Python 3           | Core development language |
| Socket Programming | Network communication     |
| ThreadPoolExecutor | Concurrent task execution |
| argparse           | Command-line interface    |

---

## Project Structure

```text id="emf51r"
port-scanner/
│
├── port_scanner.py      # Main application logic
├── README.md            # Project documentation
└── requirements.txt     # Dependencies
```

---

## Installation

Clone the repository:

```bash id="kt4wz8"
git clone <repository-url>
```

Navigate to the project directory:

```bash id="xq6a6z"
cd port-scanner
```

Run the application:

```bash id="6nk1ji"
python port_scanner.py <target>
```

---

## Usage Examples

### Basic Scan

```bash id="zexz1o"
python port_scanner.py 127.0.0.1
```

### Scan Custom Port Range

```bash id="1zx2z8"
python port_scanner.py scanme.nmap.org --start 20 --end 100
```

### Increase Concurrent Threads

```bash id="mxx47n"
python port_scanner.py 192.168.1.1 --start 1 --end 1000 --threads 200
```

---

## Core Engineering Concepts

### Concurrent Execution

The scanner leverages Python’s `ThreadPoolExecutor` to execute multiple port scans simultaneously, significantly reducing total scan time compared to sequential execution.

### Socket-Based Communication

TCP connections are established using low-level socket APIs to determine port availability and connectivity status.

### Command-Line Interface Design

The application uses argument parsing to provide a flexible and developer-friendly CLI experience.

### Scalable Architecture

The modular scanning logic allows future enhancements such as:

* UDP scanning
* Banner grabbing
* Service detection
* Logging and reporting
* GUI integration
* REST API support

---

## Sample Output

```text id="1sl3a0"
Scanning scanme.nmap.org from port 1 to 100...

[OPEN] Port 22
[OPEN] Port 80
```

---

## Security & Ethical Usage

This project is intended for:

* Educational purposes
* Networking practice
* Ethical security testing
* Authorized system analysis

Users should only scan systems they own or have explicit permission to test.

---

## Potential Improvements

* Asynchronous scanning with asyncio
* Service/version fingerprinting
* Export results to JSON/CSV
* Docker containerization
* Web dashboard integration
* Real-time progress monitoring
* Advanced timeout handling
* IPv6 support

---

## Developer Note

This project was developed as part of hands-on learning in networking, backend systems, and concurrent software engineering concepts using Python.
