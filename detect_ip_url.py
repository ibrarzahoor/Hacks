import urllib.parse
import socket

def get_ip_address(url):
    parsed_url = urllib.parse.urlparse(url)
    hostname = parsed_url.hostname
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return None

url = 'https://www.facebook.com/Kashifrb163'
ip_address = get_ip_address(url)
if ip_address:
    print("The IP address of {} is {}".format(url, ip_address))
else:
    print("Could not resolve the hostname.")
