# IP Snooper By ChatGpt

import requests  # to use this import you'd best install the requests libarary using  "pip install requests"

# Function to get public IP address of the current machine
def get_public_ip():
    try:
        # Using an external service to get the public IP address
        response = requests.get('https://api.ipify.org?format=json')
        return response.json()['ip']
    except Exception as e:
        return f"Error fetching public IP: {e}"

# Function to get detailed info about a specific IP address
def get_ip_info(ip):
    try:
        # Using an external service to get information about the IP
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        
        # Check if the status is 'success' before returning data
        if data['status'] == 'success':
            return {
                'IP': data['query'],
                'Country': data['country'],
                'Region': data['regionName'],
                'City': data['city'],
                'ISP': data['isp'],
                'Timezone': data['timezone'],
                'Latitude': data['lat'],
                'Longitude': data['lon']
            }
        else:
            return f"Error: {data['message']}"
    
    except Exception as e:
        return f"Error fetching IP info: {e}"

# Main function to snoop the IP
def snoop_ip(ip=None):
    if ip is None:
        ip = get_public_ip()
        print(f"Your public IP address: {ip}")
    else:
        print(f"Snooping info for IP address: {ip}")
    
    # Get and display detailed information about the IP
    ip_info = get_ip_info(ip)
    
    if isinstance(ip_info, dict):
        print("IP Information:")
        for key, value in ip_info.items():
            print(f"{key}: {value}")
    else:
        print(ip_info)

# Example usage:
if __name__ == "__main__":
    snoop_ip()  # Snoop your own public IP
    # snoop_ip('8.8.8.8')  # You can also snoop a specific IP address
