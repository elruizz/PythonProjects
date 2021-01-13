#Ethan Ruiz
import socket
import threading
# Connect using TCP connection to scan for ports.
def Connect(ip, port, _wait, output):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create socket connection getting (host, port) pair from AF_INET
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(_wait)
    try:
        sock.connect((ip, port))
        output[port] = 'Open'
    except:
        output[port] = 'x'

def Scan(host, _wait):
    current_threads = []
    output = {}

    for port in range(1, 65535):	# Create Thread
        t = threading.Thread(target= Connect, args=(host, port, _wait, output))
        current_threads.append(t)

    for port in range(1, 65535):	# Start Thread
        current_threads[port].start()

    for port in range(1, 65535): # Joining threads
        current_threads[port].join()

    for port in range(1, 65535): #  Output Open Ports
        if output[port] == 'Open':
            print(str(port) + ': ' + output[port])


def check_ip(s):
   try:
       return str(int(s)) == s and 0 <= int(s) <= 255
   except:
       return False

def validate(ip):
    if ip.count(".") == 3 and all(check_ip(i) for i in ip.split(".")):
       return True
    return False

def console():
    while True:
		host = input("Enter IP to Scan: ")
		if validate(host) == False:
			print('Please enter a valid IPv4 Address')
			host = input("Enter IP to Scan: ")
			break
		elif validate(host) == True:
			break

	_wait = int(input("Enter seconds before timeout: "))
	Scan(host, _wait)

def main():
    console()

if __name__ == "__main__":
    main()
