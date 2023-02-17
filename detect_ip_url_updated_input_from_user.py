import urllib.parse
import socket

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

url = get_url()
ip_address = get_ip_address(url)
if ip_address:
    print("The IP address of {} is {}".format(url, ip_address))
else:
    print("Could not resolve the hostname.")
