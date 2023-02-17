import socket

def get_ip_address():
    hostname = input("Enter the hostname you want to get the IP address for: ")
    try:
        ip_address = socket.gethostbyname(hostname)
        return hostname, ip_address
    except socket.gaierror:
        return None, None

hostname, ip_address = get_ip_address()
if ip_address:
    print("The IP address of {} is {}".format(hostname, ip_address))
else:
    print("Could not resolve the hostname.")
