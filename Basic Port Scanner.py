import socket

target = input("Enter target IP : ")
print(f"\n[🔍] Scanning {target}...\n")

# Scan ports 1 to 1024
for port in range(1, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)  # 0.5 second timeout

    result = sock.connect_ex((target, port))  # returns 0 if open
    if result == 0:
        print(f"[✅] Port {port} is OPEN")
    sock.close()

print("\n[✔] Scan complete.")

