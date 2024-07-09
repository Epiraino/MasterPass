import json
import os
from getpass import getpass
from generate_password import generate_password
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import hashlib

STORAGE_FILE = 'storage.json'
PASSWORD_HASH_FILE = 'password_hash.txt'
key = b'sixteen byte key'  # Ensure this is securely generated and stored

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def set_master_password():
    if os.path.exists(PASSWORD_HASH_FILE):
        print("Master password is already set.")
        return
    master_password = getpass("Set your master password: ")
    hashed_password = hash_password(master_password)
    with open(PASSWORD_HASH_FILE, 'w') as f:
        f.write(hashed_password)
    print("Master password has been set.")

def verify_master_password():
    if not os.path.exists(PASSWORD_HASH_FILE):
        print("Master password is not set. Please set it first.")
        return False
    with open(PASSWORD_HASH_FILE, 'r') as f:
        stored_hash = f.read().strip()
    master_password = getpass("Enter master password: ")
    if hash_password(master_password) == stored_hash:
        return True
    else:
        print("Invalid master password.")
        return False

def change_master_password():
    if verify_master_password():
        new_master_password = getpass("Enter new master password: ")
        hashed_password = hash_password(new_master_password)
        with open(PASSWORD_HASH_FILE, 'w') as f:
            f.write(hashed_password)
        print("Master password has been changed.")

# Encryption Function
def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    encrypted_data = base64.b64encode(iv + ct_bytes).decode('utf-8')
    return encrypted_data

# Decryption Function
def decrypt_data(encrypted_data, key):
    raw_data = base64.b64decode(encrypted_data)
    iv = raw_data[:16]
    ct = raw_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(ct), AES.block_size)
    return decrypted_data

# Save Passwords Function
def save_passwords(passwords_dict):
    data = json.dumps(passwords_dict).encode()
    encrypted_data = encrypt_data(data, key)
    with open(STORAGE_FILE, 'w') as file:
        file.write(encrypted_data)

# Load Passwords Function
def load_passwords():
    if not os.path.exists(STORAGE_FILE):
        return {}
    with open(STORAGE_FILE, 'r') as file:
        encrypted_data = file.read()
        decrypted_data = decrypt_data(encrypted_data, key)
        passwords_dict = json.loads(decrypted_data)
        return passwords_dict

def add_password(service, password):
    passwords = load_passwords()
    passwords[service] = password
    save_passwords(passwords)  # Pass the entire dictionary

def get_password(service):
    passwords = load_passwords()
    return passwords.get(service)

def delete_password(service):
    passwords = load_passwords()
    if service in passwords:
        del passwords[service]
        save_passwords(passwords)  # Pass the entire dictionary

def list_passwords():
    passwords = load_passwords()
    return list(passwords.keys())

def main():
    if not os.path.exists(PASSWORD_HASH_FILE):
        set_master_password()
    if not verify_master_password():
        print("Access denied.")
        return

    while True:
        print("\nMasterPass Menu")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Delete Password")
        print("4. List Services")
        print("5. Change Master Password")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            service = input("Enter the service name: ")
            password = getpass("Enter the password: ")
            add_password(service, password)
            print("Password added successfully.")
        elif choice == '2':
            service = input("Enter the service name: ")
            password = get_password(service)
            if password:
                print(f"Password for {service}: {password}")
            else:
                print("Service not found.")
        elif choice == '3':
            service = input("Enter the service name: ")
            delete_password(service)
            print("Password deleted successfully.")
        elif choice == '4':
            services = list_passwords()
            if services:
                print("Services stored:")
                for service in services:
                    print(service)
            else:
                print("No services found.")
        elif choice == '5':
            change_master_password()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")