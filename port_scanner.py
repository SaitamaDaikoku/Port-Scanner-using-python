import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def scan_port(target, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))
        sock.close()

        if result == 0:
            print(f"[OPEN] Port {port}")
    except Exception as e:
        print(f"[ERROR] Port {port}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("--start", type=int, default=1, help="Start port")
    parser.add_argument("--end", type=int, default=1024, help="End port")
    parser.add_argument("--threads", type=int, default=100, help="Number of threads")

    args = parser.parse_args()

    print(f"Scanning {args.target} from port {args.start} to {args.end}...")

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        for port in range(args.start, args.end + 1):
            executor.submit(scan_port, args.target, port)

if __name__ == "__main__":
    main()