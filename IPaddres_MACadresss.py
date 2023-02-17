import urllib.parse
import socket
import uuid

def get_url():
    url = input("Enter the URL you want to get the IP address for: ")
    return url

def get_ip_address(url):
    parsed_url = urllib.parse.urlparse(url)
    hostname = parsed_url.hostname
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return None

def get_mac_address():
    mac_address = uuid.getnode()
    return mac_address

url = get_url()
ip_address = get_ip_address(url)
mac_address = get_mac_address()

if ip_address:
    print("The IP address of {} is {}".format(url, ip_address))
else:
    print("Could not resolve the hostname.")

print("The MAC address of this machine is: {}".format(mac_address))
