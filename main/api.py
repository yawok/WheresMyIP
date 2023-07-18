import requests

def get_ip():
    BASE_URL = "https://api.ipify.org?format=json"
    response = requests.get(BASE_URL).json()
    ip = response["ip"]
    
    return ip
    
    
def get_info(ip):
    BASE_URL = f"https://ipinfo.io/{ip}/geo"
    response = requests.get(BASE_URL).json()
    return response
    
